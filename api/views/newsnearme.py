import json
from django.http import Http404
from django.db.models import Count
from django.core.cache import cache
from django.contrib.gis.geos import GEOSGeometry
from boundaryservice.models import BoundarySet, Boundary
from django.shortcuts import render, get_object_or_404


def newsnearme_list(request):
    """
    Returns list of neighborhoods and regions for Tribune's News Near Me service
    """
    context = {
        'hood_list': Boundary.objects.filter(
            set__slug='la-county-neighborhoods-v5').only("name", "slug", "simple_shape"),
        'region_list': Boundary.objects.filter(
            set__slug='la-county-regions-v5').only("name", "slug"),
    }
    response = render(request, 'api/newsnearme/getList.json', context, 
        content_type='application/javascript')
    return response


def newsnearme_detail(request):
    """
    Return the neighborhood and region that contain the provided point
    for Tribune's News Near Me service.
    """
    # Get the point the user wants
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    if not lat and not lng:
        raise Http404

    # Convert it something we can query
    point_wkt = 'POINT (%s %s)' % (lng, lat)
    point_obj = GEOSGeometry(point_wkt)

    # Figure out what areas it's in.
    try:
        hood = Boundary.objects.filter(
            set__slug='la-county-neighborhoods-v5').only(
            'name', 'slug', 'simple_shape').filter(
            shape__intersects=point_obj
        )[0]
    except IndexError:
        hood = None
    try:
        region = Boundary.objects.filter(
            set__slug='la-county-regions-v5').only(
            'name', 'slug').filter(
            shape__intersects=point_obj
        )[0]
    except IndexError:
        region = None
    context = {
        "point": point_obj,
        "hood": hood,
        "region": region,
    }
    return render(request,
        'api/newsnearme/getByLatLng.json',
        context,
        content_type='application/javascript'
    )
