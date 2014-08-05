import os, sys
import site
import newrelic.agent

sys.path.append('/apps/boundaries.latimes.com/')
sys.path.append('/apps/boundaries.latimes.com/repo/')
sys.path.append('/apps/boundaries.latimes.com/src/')
sys.path.append('/apps/boundaries.latimes.com/src/django-boundaryservice/')
sys.path.append('/apps/boundaries.latimes.com/lib/python2.7/site-packages/')
sys.path.append('/apps/boundaries.latimes.com/bin/')
site.addsitedir('/apps/boundaries.latimes.com/lib/python2.7/site-packages/')

newrelic.agent.initialize('/apps/boundaries.latimes.com/repo/project/newrelic.ini')

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
application = newrelic.agent.wsgi_application()(application)
