from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns=[
    path('',views.index,name='index'),
    path('Blogs/',views.blogs,name='blogs'),
    path('Blog/<int:blog_id>/', views.blog,name='blog'),
    path('Blog/new_blog/', views.new_blog,name='new_blog'),
    path('Blog/<int:blog_id>/edit_blog/', views.edit_blog,name='edit_blog'),
    path('Blog/<int:blog_id>/delete/', views.delete_blog,name='delete_blog'),
    path('Blog/<int:blog_id>/add_comment/', views.add_comment,name ='add_comment'),
    path('Blog/delete_comment/<int:comment_id>/',views.delete_comment,name='delete_comment'),
    path('Blog/edit_comment/<int:comment_id>/',views.edit_comment,name='edit_comment'),
]