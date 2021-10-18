from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import BlogPost, BlogComment
from .forms import BlogForm, CommentForm


def blog(request):
    """ To display all blog posts """

    blog_posts = BlogPost.objects.all().order_by("-date")

    context = {
        'blog_posts': blog_posts
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_post_id):
    """ Display blog post detail. """

    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    comments = BlogComment.objects.filter(blog_post=blog_post)

    context = {
        'blog_post': blog_post,
        'comments': comments,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog_post(request):
    """ View to add a blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            messages.success(request, 'Blog post successfully created.')
            return redirect(reverse('blog_detail', args=[blog_post.id]))
        else:
            messages.error(request, 'Failed to create blog post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_blog_post(request, blog_post_id):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post successfully updated!')
            return redirect(reverse('blog_detail', args=[blog_post.id]))
        else:
            messages.error(request, ('Failed to update blog post. '
                                     'Please ensure the form is valid.'))
    else:
        form = BlogForm(instance=blog_post)
        messages.info(request, f'You are editing {blog_post.title}')

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


@login_required
def delete_blog_post(request, blog_post_id):
    """ Delete a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    blog_post.delete()
    messages.success(request, 'Blog post deleted!')
    return redirect(reverse('blog'))


@login_required
def add_comment(request, blog_post_id):
    """ Add blog post comment """

    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog_post = blog_post
            comment.save()
            messages.success(request, 'Thank you for your comment !')
            return redirect(reverse('blog_detail', args=[blog_post.id]))
        else:
            messages.error(request,
                           'Oops something went wrong. \
                            Please try again.')
    else:
        form = CommentForm(instance=blog_post)
    template = 'blog/add_comment.html'
    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


@login_required
def edit_comment(request, comment_id):
    """ Edit a blog comment """

    comment = get_object_or_404(BlogComment, pk=comment_id)
    if request.user == comment.author or request.user.is_superuser:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(
                            request,
                            'Your comment has been successfully updated')
                return redirect(reverse('blog'))
            else:
                messages.error(request,
                               'Failed to update your comment. \
                                Please ensure the form is valid.')
        else:
            form = CommentForm(instance=comment)
        template = 'blog/edit_comment.html'
        context = {
            'form': form,
            'comment': comment,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'You can only edit your own comments!')
        return redirect(reverse('blog'))


@login_required
def delete_comment(request, comment_id):
    """ Delete a blog comment """

    comment = get_object_or_404(BlogComment, pk=comment_id)

    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')
        return redirect(reverse('blog'))
    else:
        messages.error(request, 'You cannot delete this comment!')
        return redirect(reverse('blog'))
