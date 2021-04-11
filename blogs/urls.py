from django.urls import path
from . import views
from .views import BlogView, HomeView, AddBlogView, UpdateBlogView, DeleteBlogView, BlogLikeToggle

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<slug:slug>', BlogView.as_view(), name='blog-detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('blog/edit/<slug>', UpdateBlogView.as_view(), name='update'),
    path('blog/<slug>/remove', DeleteBlogView.as_view(), name='delete'),
    path("logout/", views.logout_request, name="logout"),
    path('blogpost-like/<slug>', BlogLikeToggle.as_view(), name="blogpost_like"),
]
