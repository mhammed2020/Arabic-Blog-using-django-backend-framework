from django import template

from blog.models import Post,Comment

register = template.Library()
@register.inclusion_tag('blog/latest_posts.html')  #decorator
def latest_posts() : #simple python function

    context ={

        'l_posts' :Post.objects.all()[0:5]

    }
    return context
    

@register.inclusion_tag('blog/latest_comments.html')  #decorator
def latest_comments() : #simple python function

    context ={

        'l_comments' : Comment.objects.filter(active = True)[:5]

    }
    return context
    