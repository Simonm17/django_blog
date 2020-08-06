from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    paginate_by = 10
