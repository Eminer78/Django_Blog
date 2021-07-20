from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blogposts/blog_home.html')

def blog_post(request):
    return render(request, 'blogposts/blog_post.html')
