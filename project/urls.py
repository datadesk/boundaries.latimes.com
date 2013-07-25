import sitemaps
from django.conf import settings
from django.contrib import admin
from views import baked_file_redirects
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url
from django.views.static import serve as static_serve
from django.contrib.admin.views.decorators import staff_member_required
admin.autodiscover()

urlpatterns = patterns('',
    # Baked out urls to redirect to
    url(r'^1.0/(?P<resource_name>[\w\d_.-]+)/(?P<slug>[\w\d_.-]+)/$',
        baked_file_redirects),
    # Default urls
    (r'', include('boundaryservice.urls')),
    (r'', include('finder.urls')),
    (r'', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Pages for machines
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index',
        {'sitemaps': sitemaps.SITEMAPS}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps.SITEMAPS}),
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt',
        content_type='text/plain',
    ), name='robots-txt'),
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
