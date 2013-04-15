from django.shortcuts import render, get_object_or_404
from boundaryservice.models import BoundarySet


def boundaryset_list(request):
    """
    A list of all the available boundary sets.
    """
    context = {
        'object_list': BoundarySet.objects.all()
    }
    return render(request, 'api/boundaryset_list.html', context)


def boundaryset_detail(request, slug):
    """
    All about one BoundarySet
    """
    context = {
        'obj': get_object_or_404(BoundarySet, slug=slug)
    }
    return render(request, 'api/boundaryset_detail.html', context)
