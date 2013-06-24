import json
from django.http import Http404
from django.db.models import Count
from django.core.cache import cache
from toolbox.render_to_kmz import render_to_kmz
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.shortcuts import render_to_kml
from boundaryservice.models import BoundarySet, Boundary
from django.shortcuts import render, get_object_or_404

MIMETYPES = {
    'kml': 'application/vnd.google-earth.kml+xml',
    'kmz': 'application/vnd.google-earth.kmz',
    'json': 'application/javascript',
    'xml': 'application/xml',
}


def api_call(request, model, method, format):
    """
    Returns Mapping LA API data. 

    Services a series of models, methods and data formats.

    Models:

        * Neighborhood
        * Region

    Methods:

        getList: Returns a list of all objects in the specified model.
        getBySlug: Return the boundaries of a single object specified by slug
        getByLatLng: Return the boundaries of a single object specified by point

    Response Formats:
        
        * XML / JSON
        * KML / GeoJSON

    Example Requests:

        * Return a list of all neighborhoods as JSON

            /api/v1/neighborhood/getList.json

        * Return a list of all regions as XML

            /api/v1/region/getList.xml

        * Return the KML boundaries of Silver Lake

            /api/v1/neighborhood/getBySlug.kml?slug=silver-lake

        * Return the GeoJSON boundaries of The San Fernando Valley

            /api/v1/region/getBySlug.json?slug=san-fernando-valley

        * Return the KML of the neighborhood that contains a pair of coordinates

            /api/v1/neighborhood/getByLatLng.kml?lat=Y&lng=X

    """
    # Validate the model
    model_list = ['neighborhood', 'region', 'city']
    if model not in model_list:
        raise Http404

    # Validate the method
    method_list = ['getList', 'getBySlug', 'getByLatLng']
    if method not in method_list:
        raise Http404

    # Send the method to the appropriate view.
    method2view = {
        'getList': get_list,
        'getBySlug': get_by_slug,
        'getByLatLng': get_by_latlng,
        }
    view = method2view[method]

    string2model = {
        'neighborhood': Boundary.objects.filter(set__slug='la-county-neighborhoods-v5'),
        'region': Boundary.objects.filter(set__slug='la-county-regions-v5'),
    }
    model = string2model[model]

    return view(request, model, format)


def get_list(request, qs, format):
    """
    Serializes all of the objects in a table in XML or JSON.
    """
    # Validate format
    format_list = ['xml', 'json']
    if format not in format_list:
        raise Http404

    # Cut the template name depending on the format
    template = "api/mapping_la_v4/getList.%s" % format

    # Pull the data
    object_list = qs.only('name', 'slug',)
    context = {
        'method': 'getList',
        'model_name': qs.model._meta.verbose_name,
        'model_name_plural': qs.model._meta.verbose_name_plural,
        'object_list': object_list, 
    }

    # Set the mimetype
    mimetype = MIMETYPES[format]

    # Drop the data
    return render(request, template, context, content_type=mimetype)


def get_by_slug(request, qs, format):
    """
    Serialize an object in KML or GeoJSON.
    """
    # Validate format
    format_list = ['kml', 'json', 'kmz',]
    if format not in format_list:
        raise Http404

    # Get the slug the user wants
    slug = request.GET.get('slug', None)
    if not slug:
        raise Http404

    # Pull the data
    try:
        obj = qs.only('name', 'slug', 'shape').get(slug__startswith=slug)
    except:
        raise Http404

    context = {
        'method': 'getBySlug',
        'object': obj,
    }

    # Set the mimetype
    mimetype = MIMETYPES[format]

    # Drop the data
    if format == 'kmz':
        # Special case a KMZ request
        template = "api/mapping_la_v4/getBySlug.kml"
        response = render_to_kmz(template, context)
    else:
        # Cut the template name depending on the format
        template = "api/mapping_la_v4/getBySlug.%s" % format
        response = render(request, template, context, content_type=mimetype)

    # Set the filename for the response header
    filename = u'filename=%s.%s' % (obj.slug, format)
    response['Content-Disposition'] = filename

    # Pass everything out
    return response


def get_by_latlng(request, qs, format):
    """
    Take a users point, figure out what object it's in, pass them
    the result.
    """
    # Validate format
    format_list = ['kml', 'json', 'kmz',]
    if format not in format_list:
        raise Http404

    # Get the point the user wants
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    if not lat and not lng:
        raise Http404

    # Convert it something we can query
    point_wkt = 'POINT (%s %s)' % (lng, lat)
    point_obj = GEOSGeometry(point_wkt)

    # Figure out what object it's in.
    try:
        obj = qs.only('name', 'slug', 'shape').get(
            shape__intersects=point_obj
        )
    except:
        raise Http404

    # Load up the data
    context = {
        'method': 'getByLatLng',
        'object': obj,
        'point': point_obj,
    }

    # Set the mimetype
    mimetype = MIMETYPES[format]

    # Drop the data
    if format == 'kmz':
        # Special case a KMZ request
        template = "api/mapping_la_v4/getByLatLng.kml"
        response = render_to_kmz(template, context)
    else:
        # Cut the template name depending on the format
        template = "api/mapping_la_v4/getByLatLng.%s" % format
        response = render(request, template, context, content_type=mimetype)

    # Set the filename for the response header
    filename = u'filename=%s.%s' % (obj.slug, format)
    response['Content-Disposition'] = filename

    # Pass everything out
    return response
