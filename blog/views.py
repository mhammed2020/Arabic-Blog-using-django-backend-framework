from django.shortcuts import render

from . models import Post

# Create your views here.


posts =[
    {
'title' : 'التدوينة الاولى ',
'content' : ' نص التدوينة الاولة كنص تجريبي ',
'post_date' : '16-10-2020',
'author' : 'Jeddou Mhammed'

    },

       {
'title' : 'التدوينة التانية ',
'content' : ' نص التدوينة التانية  كنص تجريبي ',
'post_date' : '17-10-2020',
'author' : 'Saber Hmaza'

    },
       {
'title' : 'التدوينة الثالثة ',
'content' : ' نص التدوينة الثالثة كنص تجريبي ',
'post_date' : '12-10-2020',
'author' : 'Maria Medo'

    },

       {
'title' : 'التدوينة الرابعة ',
'content' : ' نص التدوينة الرابعة كنص تجريبي ',
'post_date' : '16-11-2020',
'author' : 'achraf hakimi'

    },
]


def home(request) :

    context = {
        'title' : 'الصفحة الرئيسية ',
        'posts' : Post.objects.all()
    }
    return render(request,'blog/index.html',context)

def about(request) :

    return render(request,'blog/about.html', {'title' : 'من انا'})