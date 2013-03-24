import os, sys

sys.path.append('/apps/boundaries.latimes.com/')
sys.path.append('/apps/boundaries.latimes.com/repo/')
sys.path.append('/apps/boundaries.latimes.com/src/')
sys.path.append('/apps/boundaries.latimes.com/src/django-boundaryservice/')
sys.path.append('/apps/boundaries.latimes.com/lib/python2.7/site-packages/')
sys.path.append('/apps/boundaries.latimes.com/bin/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

import site
site.addsitedir('/apps/boundaries.latimes.com/lib/python2.7/site-packages/')


from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
