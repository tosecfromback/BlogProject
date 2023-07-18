from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm, HashTagForm
from django.urls import reverse_lazy, reverse

# Create your views here.

class Index(View):
    def get(self, request):
        post_objs = Post.objects.all()
        context = {
            "posts" : post_objs,
            "title" : "Blog"
        }

        return render(request, 'blog/post_list.html', context)
    
class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:list')

class PostDetailView(DetailView):
    model = Post
    comments = Comment.objects.all()
    hashtags = HashTag.objects.all()
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    context_object_name = 'post_update'
    form_class = PostForm
    success_url = reverse_lazy('blog:list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')