# -*- coding: utf-8 -*-
"""
A unicode friendly version of render_to_kmz

Mainly to handle La Cañada Flintridge.
"""
import cStringIO, zipfile
from django.template import loader
from django.http import HttpResponse


def compress_kml(kml):
    "Returns compressed KMZ from the given KML string."
    kmz = cStringIO.StringIO()
    zf = zipfile.ZipFile(kmz, 'a', zipfile.ZIP_DEFLATED)
    zf.writestr('doc.kml', kml)
    zf.close()
    kmz.seek(0)
    return kmz.read()


def render_to_kmz(*args, **kwargs):
    """
    Compresses the KML content and returns as KMZ (using the correct 
    MIME type).
    """
    kml = loader.render_to_string(*args, **kwargs)
    kml = kml.encode('utf-8')
    kmz = compress_kml(kml)
    return HttpResponse(kmz, mimetype='application/vnd.google-earth.kmz')
