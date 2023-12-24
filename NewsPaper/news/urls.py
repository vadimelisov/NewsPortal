from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch

urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('search/', NewsSearch.as_view()),
    path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),
]
