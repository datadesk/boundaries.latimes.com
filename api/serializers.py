import csv
import StringIO
from pprint import pprint
from tastypie.serializers import Serializer
from django.template.loader import render_to_string


class GeoSerializer(Serializer):
    """
    Adds some common geospatial outputs to the standard serializer.
    
    Supported formats:
        
        * JSON (Standard issue)
        * JSONP (Standard issue)
        * KML
    
    """
    formats = [
        'json',
        'jsonp',
        'kml',
    ]
    content_types = {
        'json': 'application/json',
        'jsonp': 'text/javascript',
        'kml': 'application/vnd.google-earth.kml+xml',
    }
    
    def to_kml(self, data, options=None):
        """
        Converts the bundle to a KML serialization.
        """
        # Figure out what shape we're going to serve
        shape_type = data.request.GET.get('shape_type', 'simple')
        if shape_type == 'full':
            shape_attr = 'shape'
        else:
            shape_attr = 'simple_shape'
        # Hook the KML output to the object
        simple_obj = self.to_simple(data, options)
        simple_obj['kml'] = getattr(data.obj, shape_attr).kml
        # Render the KML using a template and pass it out
        context = {
            'obj': simple_obj,
        }
        return render_to_string('object_detail.kml', context)
