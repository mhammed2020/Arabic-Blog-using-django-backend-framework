from django import template

from blog.models import Post

register = template.Library()
@register.inclusion_tag('blog/latest_posts.html')  #decorator
def latest_posts() : #simple python function

    context ={

        'l_posts' :Post.objects.all()[0:5]

    }
    return context
    