from django.views.generic import ListView, DetailView
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Blog, id=self.kwargs['pk'])
        data['number_of_likes'] = likes_connected.number_of_likes()
        return data


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


def BlogPostLike(request, pk):
    post = get_object_or_404(Blog, id=request.POST.get('blogpost_id'))
    post.blog_likes.add(request.user)

    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))
