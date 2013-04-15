from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.static import serve as static_serve
from django.contrib.admin.views.decorators import staff_member_required
admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('boundaryservice.urls')),
    (r'', include('finder.urls')),
    (r'', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        url(r'^static/(?P<path>.*)$', 'serve', {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True,
        }),
        url(r'^media/(?P<path>.*)$', 'serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
    )


if settings.PRODUCTION:
    urlpatterns += patterns('',
        url(r'^munin/(?P<path>.*)$', staff_member_required(static_serve), {
            'document_root': settings.MUNIN_ROOT,
        })
   )
