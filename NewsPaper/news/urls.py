from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, author_now, CategoryListView, \
    subscribe
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', cache_page(60 * 1)(NewsList.as_view()), name='post_list'),
    path('search/', NewsSearch.as_view()),
    path('<int:pk>/', cache_page(60 * 5)(NewsDetail.as_view()), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('author_now/', author_now, name='author_now'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
