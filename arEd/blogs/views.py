from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
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


# def BlogPostLike(request, pk):
#     post = get_object_or_404(Blog, id=)
