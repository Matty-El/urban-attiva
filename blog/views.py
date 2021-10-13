from django.shortcuts import render
from .models import BlogPost, BlogComment


def blog(request):
    """ To display all blog posts """

    blog_posts = BlogPost.objects.all().order_by("-date")

    context = {
        'blog_posts': blog_posts
    }

    return render(request, 'blog/blog.html', context)
