from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import BlogForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class HomeView(ListView):
    model = Blog
    template_name = 'home.html'


class BlogView(DetailView):
    model = Blog
    template_name = 'details.html'
    slug_field = 'slug'

    def get_object(self):
        obj = super().get_object()
        obj.blog_views += 1
        obj.save()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Blog, slug=slug)
        l = []
        for i in obj.blog_likes.all():
            l.append(i.id)

        context['liked_user'] = l
        return context


class BlogLikeToggle(RedirectView):
    model = Blog
    template_name = 'details.html'

    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Blog, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.blog_likes.all():
                pass
            else:
                obj.blog_likes.add(user)
        return url_


class BlogLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):

        obj = get_object_or_404(Blog, slug=slug)

        user = self.request.user
        updated = False
        liked = False

        if user.is_authenticated:
            if user in obj.blog_likes.all():
                liked = False
                pass
            else:
                obj.blog_likes.add(user)
                liked = True
            updated = True
        data = {
            'updated': updated,
            'liked': liked
        }
        return Response(data)


class AddBlogView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'add_blog.html'
    # fields = ['title', 'author', 'title_image',
    #           'short_description', 'blog_content']


class UpdateBlogView(UpdateView):
    model = Blog
    template_name = 'update_blog.html'
    fields = ['title', 'short_description', 'blog_content']


class DeleteBlogView(DeleteView):
    model = Blog
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")
