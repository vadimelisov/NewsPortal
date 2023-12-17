from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post



class NewsList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    # ordering = '-time_in'


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post'