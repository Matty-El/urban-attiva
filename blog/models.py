from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class BlogPost(models.Model):
    """ Blog post model """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(
                max_length=254, null=True, blank=False,
                help_text='Minimum of 5 characters required',
                validators=[RegexValidator(
                    regex=r'^[a-zA-Z0-9,!?\.\(\)@"\'#€¥£¢$ -]+$',
                    message='Please only use text and numbers \
                        and common punctuation characters and @, or #')])
    intro = models.CharField(
                max_length=254, null=True, blank=False,
                help_text='Minimum of 10 characters required',
                validators=[RegexValidator(
                    regex=r'^[a-zA-Z0-9,!?\.\(\)@"\'#€¥£¢$ -]+$',
                    message='Please only use text and numbers \
                    and common punctuation characters and @, or #')])
    content_one = models.TextField(
                    max_length=2000, null=True, blank=False,
                    help_text='Minimum of 50 characters required',
                    validators=[RegexValidator(
                        regex=r'^[a-zA-Z0-9,!?\.\(\)@"\'#€¥£¢$ -]+$',
                        message='Please only use text and numbers \
                        and common punctuation characters and @, or #')])
    content_two = models.TextField(
                    max_length=2000, null=True, blank=True,
                    validators=[RegexValidator(
                        regex=r'^[a-zA-Z0-9,!?\.\(\)@"\'#€¥£¢$ -]+$',
                        message='Please only use text and numbers \
                        and common punctuation characters and @, or #')])
    content_three = models.TextField(
                        max_length=2000, null=True, blank=True,
                        validators=[RegexValidator(
                            regex=r'^[a-zA-Z0-9,!?\.\(\)@"\'#€¥£¢$ -]+$',
                            message='Please only use text and numbers \
                            and common punctuation characters and @, or #')])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        """ Blog post ordering """

        ordering = ['-date']


class BlogComment(models.Model):
    """ Blog comment model """

    blog_post = models.ForeignKey(BlogPost,
                                  on_delete=models.CASCADE,
                                  related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_title = models.CharField(
                    max_length=50, null=False, blank=False,
                    validators=[RegexValidator(
                        regex=r'^[a-zA-Z0-9,!?\.\(\)@"\'#€¥£¢$ -]+$',
                        message='Please only use text and numbers \
                        and common punctuation characters and @, or #')])
    comment = models.TextField(
                    max_length=2000, null=False, blank=False,
                    validators=[RegexValidator(
                        regex=r'^[a-zA-Z0-9,!?\.\(\)@"\'#€¥£¢$ -]+$',
                        message='Please only use text and numbers \
                        and common punctuation characters and @, or #')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_title

    class Meta:
        """ Ordering for blog comments """

        ordering = ['-date']
