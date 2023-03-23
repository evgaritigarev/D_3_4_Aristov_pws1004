# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleList(ListView):
    model = Article
    template_name = 'news.html'
    context_object_name = 'article'
    queryset = Article.objects.order_by('-id')


class ArticleDetail(DetailView):
    model = Article
    template_name = 'newsdetail.html'
    context_object_name = 'article'