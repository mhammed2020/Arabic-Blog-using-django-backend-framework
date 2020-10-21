from django.shortcuts import render,redirect
from .forms import UserCreationForm, LoginForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages

from django.contrib.auth import authenticate, login,logout

from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth.decorators import login_required
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
            return redirect('login')
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
            return redirect('profile')

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


@login_required(login_url='login')
def profile(request):
    # call Post with filter
    posts = Post.objects.filter(author = request.user)
    post_list = Post.objects.filter(author = request.user)

    paginator = Paginator(post_list,6)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)



    return render(request,'user/profile.html',{

        'title': 'الملف الشخصي ' ,
        'posts' : posts,
        'page':page,
        'post_list':post_list

    })

# updae profile /user in views.py

def profile_update(request):
    user_form = UserUpdateForm(instance = request.user)
    profile_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'title' :'تعديل الملف الشخصي',
        'user_form':user_form,
        'profile_form':profile_form
    }

    return render(request,'user/profile_update.html',context)

