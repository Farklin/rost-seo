from django.contrib.sitemaps import Sitemap
from .models import Uslusgi, Category, Article 

class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Category.objects.all()


class UslusgiSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Uslusgi.objects.all()

class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Article.objects.all()