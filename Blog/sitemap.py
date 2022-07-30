from django.contrib.sitemaps import Sitemap
from.models import Post
from Events.models import Event
from Pageantry.models import Pageantry


class ViewSitemap(Sitemap):
    
    changefreq = "always"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_published