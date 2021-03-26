from django.urls import path
from .views import HomeView, ArticleView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(),name='article-details'),
]
