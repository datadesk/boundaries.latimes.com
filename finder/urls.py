from django.conf.urls.defaults import patterns, include, url
from finder import views


urlpatterns = patterns('',
    url(r'^$', views.index, name="location"),
)
