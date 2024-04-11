from django.db import models
from django.contrib.auth.models import User



class Header(models.Model):
    image = models.ImageField(upload_to='img/', blank=True,verbose_name="عکس header")
    title = models.CharField(max_length=250,verbose_name="عنوان header")
    content = models.TextField()
    short_description = models.TextField()
    description = models.TextField()

class Map(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

class Request(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=11)

class TxtAdvantage(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    description = models.TextField()
    short_description = models.TextField()

class CartAdvantage(models.Model):
    image = models.ImageField(upload_to='img/', blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()

class Advantage(models.Model):
    title = models.CharField(max_length=250)

class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

class CartArticle(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img/', blank=True)
    author = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)

class DetailHeader(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img/', blank=True)

class DetailArticle(models.Model):
    image = models.ImageField(upload_to='img/', blank=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    description = models.TextField()

class ArticleDetailCart(models.Model):
    image = models.ImageField(upload_to='img/', blank=True)
    description = models.TextField()

class ImageArticle(models.Model):
    image = models.ImageField(upload_to='img/', blank=True)

class PosterArticle(models.Model):
    title = models.CharField(max_length=250)
