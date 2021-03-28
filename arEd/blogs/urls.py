from django.urls import path
from .views import BlogView, HomeView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogView.as_view(), name='blog-detail'),


]
