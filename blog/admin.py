from django.contrib import admin
from .models import BlogPost, BlogComment


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'content_one',
        'content_two',
        'content_three',
        'date',
    )

    ordering = ["-date"]


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = (
        'blog_post',
        'author',
        'comment',
        'date',
    )

    ordering = ["-date"]

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
