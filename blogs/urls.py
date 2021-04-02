from django.urls import path
from . import views
from .views import BlogView, HomeView, AddBlogView, UpdateBlogView, DeleteBlogView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogView.as_view(), name='blog-detail'),
    path('add_blog/', AddBlogView.as_view(), name='add_blog'),
    path('blog/edit/<int:pk>', UpdateBlogView.as_view(), name='update'),
    path('blog/<int:pk>/remove', DeleteBlogView.as_view(), name='delete'),
    path("logout/", views.logout_request, name="logout"),
]
