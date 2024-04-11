from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('ArticleList/', views.ArticleList.as_view(), name='article_list'),
    path('api/document/',views.api_document, name='api_document')
    ]