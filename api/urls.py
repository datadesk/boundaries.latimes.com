from django.conf.urls.defaults import patterns, include, url
from api import views


urlpatterns = patterns('',
    url(r'^sets/$', views.boundaryset_list,
        name="api-boundaryset-list"),
    url(r'^set/(?P<slug>[-\w]+)/$', views.boundaryset_detail,
        name="api-boundaryset-detail"),
)
