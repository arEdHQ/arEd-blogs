from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

# Create your views here.
class HomeView(ListView):
    model = Blog
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Blog
    template_name = 'details.html'
