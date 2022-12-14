from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.

# shubham123, shubhampatni, shubhampatni88@gmail.com

# posts = [
#     {
#         'author' : 'Shubham Patni',
#         'title' : 'Blog Post 1',
#         'content' : 'First post content',
#         'date_posted' : 'August 24, 2022'
#     },
#     {
#         'author' : 'Jane Doe',
#         'title' : 'Blog Post 2',
#         'content' : 'Second post content',
#         'date_posted' : 'August 28, 2022'
#     }
# ]

# def home(request):
#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request,'home.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post 


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post 
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # check if correct author is updating post
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False

def about(request):
    return render(request,'about.html')

@login_required
def user_post(request):
    object = {
        'posts' : Post.objects.filter(author = request.user)
    }
    return render(request,'user_post.html', object)


# def add_post(request):
#     if request.method == 'POST':
          