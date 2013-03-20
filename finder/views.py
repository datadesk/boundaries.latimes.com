import json
from django.conf import settings
from django.shortcuts import render
from django.template import RequestContext


def index(request):
    context = {}
    # Serialize JSON settings to context
    select_settings = {
      'EXAMPLE_SCOPE': settings.EXAMPLE_SCOPE,
      'EXAMPLE_PLACE': settings.EXAMPLE_PLACE,
      'EXAMPLE_PLACE_LAT_LNG': settings.EXAMPLE_PLACE_LAT_LNG,
      'EXAMPLE_UNIT': settings.EXAMPLE_UNIT,
      'EXAMPLE_UNIT_CODE': settings.EXAMPLE_UNIT_CODE,
      'EXAMPLE_PLACE_BBOX': settings.EXAMPLE_PLACE_BBOX
    }
    context['settings'] = select_settings
    context['json_settings'] = json.dumps(select_settings)
    try:
        address = request.REQUEST.get('address')
        context['address'] = address
    except KeyError:
        pass
    return render(request, 'finder/index.html', context)
