from rest_framework import serializers
from .models import *


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class TxtAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TxtAdvantage
        fields = '__all__'


class CartAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartAdvantage
        fields = '__all__'


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'



class CartArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartArticle
        fields = '__all__'


class DetailHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailHeader
        fields = '__all__'


class DetailArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailArticle
        fields = '__all__'

class ArticleDetailCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetailCart
        fields = '__all__'

class ImageArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageArticle
        fields = '__all__'

class PosterArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosterArticle
        fields = '__all__'



