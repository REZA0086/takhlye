from django.contrib import admin
from .models import *


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','short_description')

@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Request)
class Request(admin.ModelAdmin):
    list_display = ('name','phone')

@admin.register(TxtAdvantage)
class TxtAdvantage(admin.ModelAdmin):
    list_display = ('title','content','short_description')

@admin.register(CartAdvantage)
class CpAdvantageAdmin(admin.ModelAdmin):
    list_display = ('title','description')

@admin.register(Advantage)
class Advantage(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','description']

@admin.register(CartArticle)
class CartArticle(admin.ModelAdmin):
    list_display = ['title','author']

@admin.register(DetailHeader)
class DetailHeader(admin.ModelAdmin):
    list_display = ['title']

@admin.register(DetailArticle)
class DetailArticle(admin.ModelAdmin):
    list_display = ['title','author']

@admin.register(ArticleDetailCart)
class ArticleDetailCart(admin.ModelAdmin):
    list_display = ['description']

@admin.register(ImageArticle)
class ImageArticle(admin.ModelAdmin):
    list_display = ['image']

@admin.register(PosterArticle)
class PosterArticle(admin.ModelAdmin):
    list_display = ['title']
