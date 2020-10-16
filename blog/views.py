from django.shortcuts import render

from . models import Post

# Create your views here.

def home(request) :

    context = {
        'title' : 'الصفحة الرئيسية ',
        'posts' : Post.objects.all()
    }
    return render(request,'blog/index.html',context)

def about(request) :

    return render(request,'blog/about.html', {'title' : 'من انا'})