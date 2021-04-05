from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import BlogForm


class HomeView(ListView):
    model = Blog
    template_name = 'home.html'


class BlogView(DetailView):
    model = Blog
    template_name = 'details.html'
    slug_field='slug'

    def get_object(self):
        obj = super().get_object()
        obj.blog_views += 1
        obj.save()
        return obj


class BlogLikeRedirect(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Blog, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            obj.blog_likes.add(user)
        return url_


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

