from tastypie.api import Api
from boundaryservice.views import external_id_redirects
from django.conf.urls.defaults import patterns, include, url
from api.resources import LATBoundarySetResource, LATBoundaryResource

v1_api = Api(api_name='1.0')
v1_api.register(LATBoundarySetResource())
v1_api.register(LATBoundarySetResource())

urlpatterns = patterns('',
    
    # Custom override of the standard django-boundaryservice
    (r'^(?P<api_name>1.0)/(?P<resource_name>boundary-set)/(?P<slug>[\w\d_.-]+)/(?P<external_id>[\w\d_.-]+)$', external_id_redirects),
    (r'', include(v1_api.urls)),
    
    # Public facing pages to display data
    url(r'^sets/$', 'api.views.finder.boundaryset_list',
        name="api-boundaryset-list"),
    url(r'^set/(?P<slug>[-\w]+)/$', 'api.views.finder.boundaryset_detail',
        name="api-boundaryset-detail"),
    
    # Help
    url(r'^about/$', 'api.views.finder.about',
        name="api-about"),
    
    # News Near Me custom API endpoints
    url(r'^api/v1/news-near-me/getList.json$',
        'api.views.newsnearme.newsnearme_list',
        name="api-newsnearme-list"),
    url(r'^api/v1/news-near-me/getByLatLng.json$',
        'api.views.newsnearme.newsnearme_detail',
        name="api-newsnearme-detail"),
    
    # Mapping LA (V4) API urls
    url(r'^api/v1/(?P<model>[-\w]+)/(?P<method>[-\w]+).(?P<format>[-\w]+)/$',
        'api.views.mapping_la_v4.api_call',
        name="mapping-la-v4-api-call"),
    
    # Mapping LA (V1) API urls
    url(r'^api/neighborhoods/neighborhood/(?P<slug>[-\w]+)/kml/boundaries.kml$', 
        'api.views.mapping_la_v1.neighborhood_kml',
        name="mapping-la-v1-kml-by-hood"),
    url(r'^api/neighborhoods/region/(?P<slug>[-\w]+)/kml/boundaries.kml$', 
        'api.views.mapping_la_v1.region_kml',
        name="mapping-la-v1-kml-by-region"),
    url(r'^api/neighborhoods/slugs/json/$',
        'api.views.mapping_la_v1.slugs_json',
        name="mapping-la-v1-slug-json"),

)
