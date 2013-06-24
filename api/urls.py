from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    
    # Public facing pages to display data
    url(r'^sets/$', 'api.views.finder.boundaryset_list',
        name="api-boundaryset-list"),
    url(r'^set/(?P<slug>[-\w]+)/$', 'api.views.finder.boundaryset_detail',
        name="api-boundaryset-detail"),
    
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
    
)
