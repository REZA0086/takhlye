from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from rest_framework.decorators import api_view
from .forms import *
from .models import *
from django.views.generic import View, TemplateView, DetailView
from rest_framework.response import Response
from .serializers import *

# Create your views here.
def media_admin(request):
    return {'media_url': settings.MEDIA_URL,}






class Index(View):
    def get(self,request,*args,**kwargs):
        map = Map.objects.all().first()
        form = MapForm()
        header = Header.objects.all().first()
        txt_advantage = TxtAdvantage.objects.all().first()
        cart_advantages = CartAdvantage.objects.all()
        advantage = Advantage.objects.all()
        article = Article.objects.all().first()
        cart_article = CartArticle.objects.all()
        context = {
            'map' : map,
            'form' : form,
            'header': header,
            'txt_advantage' : txt_advantage,
            'cart_advantages' : cart_advantages,
            'advantage' :advantage,
            'article' : article,
            'cart_article' : cart_article
        }
        return render(request,'index.html',context)

    def post(self,request,*args,**kwargs):
        form = MapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        context = {
            'map': map,
            'form': form
        }
        return render(request,'index.html',context)

class ArticleList(DetailView):
    def get(self,request,*args,**kwargs):
        header = DetailHeader.objects.all().first()
        article = DetailArticle.objects.all().first()
        cart_article = ArticleDetailCart.objects.all()
        image_article = ImageArticle.objects.all()
        poster_article = PosterArticle.objects.all()
        context ={
            'header' : header,
            'article' : article,
            'cart_article' : cart_article,
            'image_article' : image_article,
            'poster_article' : poster_article
        }
        return render(request,'detail.html',context)
    def post(self,request,*args,**kwargs):
        return render(request, 'detail.html')


@api_view(['GET'])
def api_document(request, *args, **kwargs):
    header_data = Header.objects.all()
    map_data = Map.objects.all()
    request_form_data = Request.objects.all()
    txt_advantage_data = TxtAdvantage.objects.all()
    cart_advantage_data = CartAdvantage.objects.all()
    advantage_data = Advantage.objects.all()
    article_data = Article.objects.all()
    cart_article_data = CartArticle.objects.all()
    detail_article_data = DetailArticle.objects.all()
    article_detail_cart_data = ArticleDetailCart.objects.all()
    image_article_data = ImageArticle.objects.all()
    poster_article_data = PosterArticle.objects.all()

    header_serializers = HeaderSerializer(header_data, many=True)
    map_serializers = MapSerializer(map_data, many=True)
    request_form_serializers = RequestSerializer(request_form_data, many=True)
    txt_advantage_serializers = TxtAdvantageSerializer(txt_advantage_data, many=True)
    cart_advantage_serializers = CartAdvantageSerializer(cart_advantage_data, many=True)
    advantage_serializers = AdvantageSerializer(advantage_data, many=True)
    article_serializers = ArticleSerializer(article_data, many=True)
    cart_article_serializers = CartArticleSerializer(cart_article_data, many=True)
    detail_article_serializers = DetailArticleSerializer(detail_article_data, many=True)
    article_detail_cart_serializers = ArticleDetailCartSerializer(article_detail_cart_data, many=True)
    image_article_serializers = ImageArticleSerializer(image_article_data, many=True)
    poster_article_serializers = PosterArticleSerializer(poster_article_data, many=True)

    data = {
        'Header': header_serializers.data,
        'Map': map_serializers.data,
        'Request': request_form_serializers.data,
        'TxtAdvantage': txt_advantage_serializers.data,
        'CartAdvantage': cart_advantage_serializers.data,
        'Advantage': advantage_serializers.data,
        'Article': article_serializers.data,
        'CartArticle': cart_article_serializers.data,
        'DetailArticle': detail_article_serializers.data,
        'ArticleDetailCart': article_detail_cart_serializers.data,
        'ImageArticle': image_article_serializers.data,
        'PosterArticle': poster_article_serializers.data,
    }

    return Response(data)

