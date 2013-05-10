import json
from django.db.models import Count
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
