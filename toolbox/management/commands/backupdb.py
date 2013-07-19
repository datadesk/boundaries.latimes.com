"""
A postgres database backup script lifted from Samuel Clay's Newsblur
https://github.com/samuelclay/NewsBlur
"""
import os
import sys
import time
import boto
import datetime
from boto.s3.key import Key
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

CHUNK_DIR = '/tmp/chunk_dir'
os.path.exists(CHUNK_DIR) or os.mkdir(CHUNK_DIR)


class Command(BaseCommand):
    help = 'Back up the database to Amazon S3'
    site = 'boundaries.latimes.com'
    bucket = 'databank-archive.latimes.com'
    
    def split_file(self, input_file, chunk_size=900000000):
        file_size = os.path.getsize(input_file)
        f = open(input_file, 'rb')
        data = f.read()
        f.close()
        
        if not os.path.exists(CHUNK_DIR):
            os.makedirs(CHUNK_DIR)
        
        bytes = len(data)
        num_chunks = bytes  / chunk_size
        if(bytes%chunk_size):
            num_chunks  += 1
        
        chunk_names = []
        for i in range(0, bytes + 1, chunk_size):
            chunk_name = "chunk%s" % i
            chunk_names.append(chunk_name)
            f = open(CHUNK_DIR+'/'+chunk_name, 'wb')
            f.write(data[i:i+chunk_size])
            f.close()
    
    def handle(self, *args, **options):
        db_user = settings.DATABASES['default']['USER']
        db_name = settings.DATABASES['default']['NAME']
        db_pass = settings.DATABASES['default']['PASSWORD']
        os.environ['PGPASSWORD'] = db_pass
        
        filename = 'postgres_default_%s.sql.gz' % (
            time.strftime('%Y-%m-%d')
        )
        cmd = 'pg_dump -U %s -Fc %s > %s' % (db_user, db_name, filename)
        
        print 'Backing up PostgreSQL: %s' % cmd
        os.system(cmd)
        
        print 'Connecting to S3'
        conn = boto.connect_s3(
            settings.AWS_ACCESS_KEY_ID,
            settings.AWS_SECRET_ACCESS_KEY
        )
        bucket = conn.get_bucket(self.bucket)
        
        target = '%s/%s' % (self.site, filename)
        latest = "%s/postgres_default_latest.sql.gz" % self.site
    
        print "Uploading %s" % target
        mp = bucket.initiate_multipart_upload(target, reduced_redundancy=False,
            policy='bucket-owner-full-control')
        self.split_file(filename)
        file_list = os.listdir(CHUNK_DIR)
        i = 1
        for file_part in file_list:
            with open(CHUNK_DIR+'/'+file_part) as f:
                mp.upload_part_from_file(f, i)
            os.remove(CHUNK_DIR+'/'+file_part)
            i += 1
        mp.complete_upload()
        
        # Create a 'latest' copy and make both public
        key = bucket.lookup(mp.key_name)
        copy = key.copy(self.bucket, latest)
        
        print "Deleting %s" % filename
        os.remove(filename)

