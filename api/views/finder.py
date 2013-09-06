import json
from django.conf import settings
from django.http import Http404
from django.db.models import Count
from django.core.cache import cache
from django.contrib.gis.geos import GEOSGeometry
from boundaryservice.models import BoundarySet, Boundary
from django.shortcuts import render, get_object_or_404


def about(request):
    """
    A page that explains what the site is about.
    """
    context = {}
    return render(request, 'api/about.html', context)


def boundaryset_list(request):
    """
    A list of all the available boundary sets.
    """
    context = {
        'object_list': BoundarySet.objects.all(),
        'source_count': BoundarySet.objects.values('authority').distinct().count(),
        'feature_count': Boundary.objects.count()
    }
    return render(request, 'api/boundaryset_list.html', context)


def boundaryset_detail(request, slug):
    """
    All about one BoundarySet
    """
    select_settings = {
      'EXAMPLE_SCOPE': settings.EXAMPLE_SCOPE,
      'EXAMPLE_PLACE': settings.EXAMPLE_PLACE,
      'EXAMPLE_PLACE_LAT_LNG': settings.EXAMPLE_PLACE_LAT_LNG,
      'EXAMPLE_UNIT': settings.EXAMPLE_UNIT,
      'EXAMPLE_UNIT_CODE': settings.EXAMPLE_UNIT_CODE,
      'EXAMPLE_PLACE_BBOX': settings.EXAMPLE_PLACE_BBOX
    }
    obj = get_object_or_404(BoundarySet, slug=slug)
    boundary_list = obj.boundaries.all()
    context = {
        'obj': obj,
        'boundary_list': boundary_list,
        'settings': select_settings,
        'json_settings': json.dumps(select_settings),
        'ARCHIVE_BASE_URL': settings.ARCHIVE_BASE_URL,
    }
    return render(request, 'api/boundaryset_detail.html', context)
