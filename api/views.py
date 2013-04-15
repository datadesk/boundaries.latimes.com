from django.shortcuts import render
from boundaryservice.models import BoundarySet


def boundaryset_list(request):
    """
    A list of all the available boundary sets.
    """
    context = {
        'object_list': BoundarySet.objects.all()
    }
    return render(request, 'api/boundaryset_list.html', context)
