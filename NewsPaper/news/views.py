from allauth.core.internal.http import redirect
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = '-date_in'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post'


class NewsSearch(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'



class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'



class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = '/news/'


def author_now(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not user.groups.filter(name='authors').exists():
        user.groups.add(author_group)
    return redirect('post_list')