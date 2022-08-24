from django.shortcuts import render
from .models import Post

# Create your views here.

# shubham123, shubhampatni, shubhampatni88@gmail.com

posts = [
    {
        'author' : 'Shubham Patni',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'August 24, 2022'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'August 28, 2022'
    }
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'home.html', context)


def about(request):
    return render(request,'about.html')