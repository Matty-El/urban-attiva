from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import BlogPost, BlogComment
from .forms import BlogForm, CommentForm


def blog(request):
    """ To display all blog posts """

    query = None
    sort = None
    direction = None

    blog_posts = BlogPost.objects.all().order_by("-date")

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('blog'))

            queries = Q(title__icontains=query) | Q(intro__icontains=query)
            blog_posts = blog_posts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'blog_posts': blog_posts,
        'search_term': query,
        'current_sorting': current_sorting,
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
        content_two = form['content_two'].data
        content_three = form['content_three'].data
        if content_two.isspace() or content_three.isspace() is True:
            messages.error(request, ('Failed to update blog post. '
                                     'Please do not enter only blank spaces in'
                                     ' content form fields.'))
        else:
            if form.is_valid():
                blog_post = form.save()
                messages.success(request, 'Blog post successfully created.')
                return redirect(reverse('blog_detail', args=[blog_post.id]))
            else:
                messages.error(
                    request,
                    'Failed to create blog post. '
                    'Please ensure the form is valid.')
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
        content_two = form['content_two'].data
        content_three = form['content_three'].data
        if content_two.isspace() or content_three.isspace() is True:
            messages.error(request, ('Failed to update blog post. '
                                     'Please do not enter only blank spaces in'
                                     ' content form fields.'))

        else:
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
                           'Failed to add comment. \
                            Please ensure the form is valid.')
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
    """ Edit a blog post comment """

    comment = get_object_or_404(BlogComment, pk=comment_id)
    blog_post = comment.blog_post

    if request.user == comment.author or request.user.is_superuser:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(
                            request,
                            'Your comment has been successfully updated')
                return redirect(reverse('blog_detail', args=[blog_post.id]))
            else:
                messages.error(request,
                               'Failed to update your comment. \
                                Please ensure the form content is valid.')
        else:
            form = CommentForm(instance=comment)
        template = 'blog/edit_comment.html'
        context = {
            'form': form,
            'comment': comment,
            'blog_post': blog_post,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'You can only edit your own comments!')
        return redirect(reverse('blog_detail', args=[blog_post.id]))


@login_required
def delete_comment(request, comment_id):
    """ Delete a blog post comment """

    comment = get_object_or_404(BlogComment, pk=comment_id)
    blog_post = comment.blog_post

    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')
        return redirect(reverse('blog_detail', args=[blog_post.id]))
    else:
        messages.error(request, 'You cannot delete this comment!')
        return redirect(reverse('blog_detail', args=[blog_post.id]))

    context = {
        'blog_post': blog_post,
    }

    return render(request, context)
