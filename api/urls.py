from django.conf.urls.defaults import patterns, include, url
from api import views


urlpatterns = patterns('',
    
    # Public facing pages to display data
    url(r'^sets/$', views.boundaryset_list,
        name="api-boundaryset-list"),
    url(r'^set/(?P<slug>[-\w]+)/$', views.boundaryset_detail,
        name="api-boundaryset-detail"),
    
    # News Near Me custom API endpoints
    url(r'^api/v1/news-near-me/getList.json$', views.newsnearme_list,
        name="api-newsnearme-list"),
    url(r'^api/v1/news-near-me/getByLatLng.json$', views.newsnearme_detail,
        name="api-newsnearme-detail"),

)
