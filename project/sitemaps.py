from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from boundaryservice.models import BoundarySet


class AbstractSitemapClass():
    url = None
    
    def get_absolute_url(self):
        return self.url


class StaticSitemap(Sitemap):
    pages = {
        'finder':'/',
        'api-boundaryset-list':'/sets/',
    }
    main_sitemaps = []
    for page in pages.keys():
        sitemap_class = AbstractSitemapClass()
        sitemap_class.url = pages[page]
        main_sitemaps.append(sitemap_class)
    
    def items(self):
        return self.main_sitemaps


class BoundarySetSitemap(Sitemap):
    changefreq = "monthly"
    limit = 1000
    
    def items(self):
        return BoundarySet.objects.all()
    
    def location(self, obj):
        return reverse('api-boundaryset-detail', args=[obj.slug])


SITEMAPS = {
    'static': StaticSitemap,
    'sets': BoundarySetSitemap,
}
