from django.shortcuts import render,get_object_or_404

from . models import Post,Comment

from .forms import NewComment, PostCreateForm
# Create your views here.
#CBVs style with  for create posts
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


#pagination 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#=======================================================================
def home(request) :
    posts = Post.objects.all()
    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)

    context = {
        'title' : 'الصفحة الرئيسية ',
        'posts' : posts,
        'page':page
    }
    return render(request,'blog/index.html',context)

def about(request) :

    return render(request,'blog/about.html', {'title' : 'من انا'})


def post_detail(request,post_id) :

    post = get_object_or_404(Post,pk=post_id)
    comments = post.comments.filter(active=True)


    if request.method == 'POST' :
        comment_form = NewComment(data = request.POST)

        if comment_form.is_valid() :
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else :
        comment_form = NewComment()

    context ={
        'title':post,
        'post' : post,
        'comments':comments,
        'comment_form' :comment_form, 
    }

   
    return render(request,'blog/detail.html', context)

#CBVs .. Usage 

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    # fields = ['title', 'content']
    template_name = 'blog/new_post.html'

    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)