from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    #path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    #path('add_comment/', views.add_comment, name='add_comment'),
    #path('blog_detail/', views.blog_detail, name='blog_detail'),
    #path('edit_blog_post/', views.edit_blog_post, name='blog'),
    #path('edit_comment/', views.edit_comment, name='edit_comment'),
]