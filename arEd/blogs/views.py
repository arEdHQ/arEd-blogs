from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Blog
from django.http import HttpResponseRedirect
from django.urls import reverse


class HomeView(ListView):
    model = Blog
    template_name = 'home.html'


class BlogView(DetailView):
    model = Blog
    template_name = 'details.html'

    def get_object(self):
        obj = super().get_object()
        obj.blog_views += 1
        obj.save()
        return obj


class AddBlogView(CreateView):
    model = Blog
    template_name = 'add_blog.html'
    fields = '__all__'


class UpdateBlogView(UpdateView):
    model = Blog
    template_name = 'update_blog.html'
    fields = ['title', 'short_description', 'blog_content']

# def BlogPostLike(request, pk):
#     post = get_object_or_404(Blog, id=)
