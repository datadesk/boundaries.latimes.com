import boto
from boto.s3.key import Key
from django.conf import settings
from optparse import make_option
from django.core.urlresolvers import resolve
from django.test.client import RequestFactory
from boundaryservice.models import BoundarySet
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Bake big files to S3'
    option_list = BaseCommand.option_list + (
        make_option('-o', '--only', action='store', dest='only',
            default=False, help='Only load the provided boundary sets. Accepts a comma-delimited list of slugs.'),
    )
    bucket = 'boundaries.latimes.com'
    ext = {
        'json': 'json',
        'geojson': 'geojson',
        'kml': 'kml',
        'shp': 'zip',
    }
    content_type = {
        'json': 'application/json',
        'geojson': 'application/geo+json',
        'kml': 'application/vnd.google-earth.kml+xml',
        'shp': 'application/zip',
    }
    
    def handle(self, *args, **options):
        # Connect to S3
        conn = boto.connect_s3(
            settings.AWS_ACCESS_KEY_ID,
            settings.AWS_SECRET_ACCESS_KEY,
        )
        bucket = conn.get_bucket(self.bucket)
        # Limit the sets if 'only' list provided
        obj_list = BoundarySet.objects.all()
        if options['only']:
            only = [s.strip() for s in options['only'].split(',') if s.strip()]
            obj_list = obj_list.filter(slug__in=only)
        # Loop thru the BoundarySets and do the job
        for bs in obj_list:
            url = "/1.0/boundary-set/%s/" % bs.slug
            for format in ['json', 'geojson', 'kml', 'shp']:
                print "- Archiving %s in %s" % (bs.slug, format)
                # Get the data
                func, args, kwargs = resolve(url)
                request = RequestFactory().get(url + "?format=%s" % format)
                data = func(request, *args, **kwargs).content
                # Upload it to S3
                k = Key(bucket)
                k.key = "archive/1.0/boundary-set/%(slug)s.%(ext)s" % dict(
                    slug=bs.slug,
                    ext=self.ext[format]
                )
                k.set_metadata('Content-Type', self.content_type[format])
                k.set_contents_from_string(data)
                k.set_acl('public-read')
