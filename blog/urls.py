from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path('add_comment/<int:blog_post_id>/', views.add_comment,
         name='add_comment'),
    path('blog_detail/<int:blog_post_id>/', views.blog_detail,
         name='blog_detail'),
    path('edit_blog_post/<int:blog_post_id>/', views.edit_blog_post,
         name='edit_blog_post'),
    path('edit_comment/<int:comment_id>/', views.edit_comment,
         name='edit_comment'),
    path('delete_blog_post/<int:blog_post_id>/', views.delete_blog_post,
         name='delete_blog_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment,
         name='delete_comment')
]
