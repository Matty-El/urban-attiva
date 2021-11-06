from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re


class BlogPost(models.Model):
    """ Blog post model """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254, null=True, blank=False)
    intro = models.CharField(max_length=254, null=True, blank=False)
    content_one = models.TextField(max_length=2000, null=True, blank=False)
    content_two = models.TextField(max_length=2000, null=True, blank=True)
    content_three = models.TextField(max_length=2000, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class BlogComment(models.Model):
    """ Blog comment model """

    blog_post = models.ForeignKey(BlogPost,
                                  on_delete=models.CASCADE,
                                  related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_title = models.CharField(max_length=50, null=False, blank=False)
    comment = models.TextField(max_length=2000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_title

    class Meta:
        """ Ordering for blog comments """

        ordering = ['-date']
