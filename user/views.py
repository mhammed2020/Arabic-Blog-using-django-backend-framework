from django.shortcuts import render,redirect
from .forms import UserCreationForm, LoginForm
from django.contrib import messages

from django.contrib.auth import authenticate, login,logout

from blog.models import Post
def register(request) :


    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            new_user = form.save(commit=False)
            # username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            messages.success(
                request,' تهانينا {}  لقد تمت عملية التسجيل بنجاح  '.format(new_user)
            )
            return redirect('home')
    else :
        form = UserCreationForm()

    return render(request,'user/register.html', { 
   'title' : 'التسجيل ',
   'form' :form

    })

    # login form  user app

def login_user(request) :

    if request.method=='POST':
        # form = LoginForm() changed with html form
        # catch inputs 
        username = request.POST['username']
        password = request.POST['password']
        # authenticate function
        user = authenticate(request,username=username, password =password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else :
            messages.warning(
                request,' هناك خطأ في اسم المستخدم أو كلمة المرور ')

    # else :
    #     form = LoginForm() changed with html form
    
    return render(request,'user/login.html',{
        'title' :'تسجيل الدخول',
        # 'form':form, 
        })

# logout function

def logout_user(request):
    logout(request)

    return render(request,'user/logout.html',
    
    {
        'title' : 'تسجيل الخروج'
         
    })

    # create profile for Users


def profile(request):
    # call Post with filter
    posts = Post.objects.filter(author = request.user)
    return render(request,'user/profile.html',{

        'title': 'الملف الشخصي ' ,
        'posts' : posts

    })
