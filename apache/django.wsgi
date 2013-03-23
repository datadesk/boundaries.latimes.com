import os, sys
sys.path.append('/apps/boundaries.latimes.com/')
sys.path.append('/apps/boundaries.latimes.com/repo/')
sys.path.append('/apps/boundaries.latimes.com/lib/python2.7/site-packages/')
sys.path.append('/apps/boundaries.latimes.com/bin/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
