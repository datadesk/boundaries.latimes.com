import json
from django.db.models import Count
from django.core.cache import cache
from boundaryservice.models import BoundarySet, Boundary
from django.shortcuts import render, get_object_or_404


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
    obj = get_object_or_404(BoundarySet, slug=slug)
    boundary_list = obj.boundaries.all()
    context = {
        'obj': obj,
        'boundary_list': boundary_list
    }
    return render(request, 'api/boundaryset_detail.html', context)


def newsnearme_list(request):
    """
    Returns list of neighborhoods and regions for Tribune's News Near Me service
    """
    cache_key = "newsnearme_list"
    cached_response = cache.get(cache_key, None)
    if cached_response:
        return cached_response
    context = {
        'hood_list': Boundary.objects.filter(
            set__slug='los-angeles-county-neighborhoods-v5').only("name", "slug", "simple_shape"),
        'region_list': Boundary.objects.filter(
            set__slug='los-angeles-county-regions-v5').only("name", "slug"),
    }
    response = render(request, 'api/newsnearme/getList.json', context, 
        content_type='application/javascript')
    cache.set(cache_key, response, 60 * 60 * 72 * 2)
    return response
