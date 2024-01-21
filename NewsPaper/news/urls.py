from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, author_now

urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('search/', NewsSearch.as_view()),
    path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
    path('author_now/', author_now, name='author_now')
]
