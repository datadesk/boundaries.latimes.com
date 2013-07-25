from django.http import Http404
from django.conf import settings
from django.shortcuts import redirect


def baked_file_redirects(request, resource_name, slug):
    """
    Redirect baked out data to S3 instead of serving out of the database.
    """
    allowed_formats = {
        'json': 'json',
        'geojson': 'geojson',
        'kml': 'kml',
        'shp': 'zip',
    }
    f = request.GET.get('format', 'json')
    if f not in allowed_formats.keys():
        raise Http404
    url = settings.ARCHIVE_BASE_URL + request.path[:-1] + "." + allowed_formats[f]
    return redirect(url, permanent=False)
