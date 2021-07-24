from django.shortcuts import render
from .models import Blogpost

# Create your views here.

def index(request):
    count = Blogpost.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'blogposts/blog_home.html',context)

def blog_post(request):
    return render(request, 'blogposts/blog_post.html')

def about(request):
    return render(request,'blogposts/about.html')
