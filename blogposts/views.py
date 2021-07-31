from django.shortcuts import render
from .models import Blogpost

# Create your views here.

def index(request):
    count = Blogpost.objects.all().count()
    context = {
        'count': count,
        'title_text': 'The Adventures of Penny the Pitbull',
    }
    return render(request, 'blogposts/blog_home.html',context)


def blog_adventures(request):
    context = {
        'title_text': 'Recent Adventures',
        'blogposts': Blogpost.objects.all(),
    }
    return render(request, 'blogposts/blog_adventures.html', context)


def blog_post(request, post_id):
    context = {
        'title_text': '',
        'post': Blogpost.objects.get(id=post_id)
    }
    return render(request, 'blogposts/blog_post.html', context)


def new_adventure(request):
    if request.method == "POST":
        print('POST request')
        new_post = Blogpost.objects.create(
            title = request.POST['title'],
            author = request.POST['author'],
            description = request.POST['description'],
        )
        new_adventure.save()  
        context = {
            'title_text': 'your post "' + request.POST['title'] + '" has been created'
        }
        return render(request, 'blogposts/new_adventure.html', context)       
    elif request.method == "GET": 
        print('GET request')
        context = {
            'title_text': 'new Adventure'
        }
        return render(request, 'blogposts/new_adventure.html', context)


def about(request):
    context = {
        'title_text': 'about',
    }
    return render(request,'blogposts/about.html', context)