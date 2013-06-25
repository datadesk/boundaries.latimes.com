import json
from django.http import Http404
from django.db.models import Count
from django.core.cache import cache
from toolbox.render_to_kmz import render_to_kmz
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.shortcuts import render_to_kml
from boundaryservice.models import BoundarySet, Boundary
from django.shortcuts import render, get_object_or_404


def neighborhood_kml(request, slug):
    """
    Returns the KML for a particular neighborhood.
    """
    try:
        qs = Boundary.objects.filter(set__slug='la-county-neighborhoods-v5')
        obj = qs.get(slug__startswith=slug)
    except Boundary.DoesNotExist:
        raise Http404
    except Boundary.MultipleObjectsReturned:
        l = qs.filter(slug__startswith=slug)
        obj = [i for i in l if i.metadata['slug'] == slug][0]
    return render_to_kml("api/mapping_la_v1/hood.kml", locals())


def region_kml(request, slug):
    """
    Return the KML for a particular region.
    """
    try:
        qs = Boundary.objects.filter(set__slug='la-county-regions-v5')
        obj = qs.get(slug__startswith=slug)
    except Boundary.DoesNotExist:
        raise Http404
    return render_to_kml("api/mapping_la_v1/region.kml", locals())


def slugs_json(request):
    """
    Returns a JSON object with all the valid neighborhood and region slugs.
    
    Can be used by mappingla.com's url shortener to validate requests.
    """
    hood_list = Boundary.objects.filter(
        set__slug='la-county-neighborhoods-v5').values('name')
    region_list = Boundary.objects.filter(
        set__slug='la-county-regions-v5').values('name')
    return render(request, 'api/mapping_la_v1/slugs.json', {
        'hood_list': hood_list,
        'region_list': region_list,
    }, content_type="text/javascript")
