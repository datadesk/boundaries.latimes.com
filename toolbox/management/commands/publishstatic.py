import os
import subprocess
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Syncs the static directory to Amazon S3"
    
    def handle(self, *args, **kwds):
        if not os.path.exists(settings.STATIC_ROOT):
            raise CommandError("Static directory does not exist. Cannot publish something before you build it.")
        cmd = "s3cmd sync --delete-removed --config=%(config)s --acl-public %(static)s/ s3://%(bucket)s/static/"
        subprocess.call(cmd % dict(
            config=os.path.join(settings.ROOT_DIR, 's3cmd', settings.AWS_BUCKET_NAME),
            static=settings.STATIC_ROOT,
            bucket=settings.AWS_BUCKET_NAME
        ), shell=True)
