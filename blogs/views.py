from django.shortcuts import render, redirect
from .models import Blog,Comment
from .forms import Blogform,Commentform
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request):
    blogs = Blog.objects.order_by('-date_added')
    context={'blogs':blogs[:4]}
    return render(request,'blogs/index.html',context)

def blogs(request):
    blogs = Blog.objects.order_by('-date_added')
    context={'blogs':blogs}
    return render(request,'blogs/blogs.html',context)

@login_required
def blog(request, blog_id):
    blog=Blog.objects.get(id=blog_id)
    comments=blog.comment_set.order_by('-date_added')
    context={'blog':blog,'comments':comments}
    return render(request,'blogs/blog.html',context)

@login_required
def new_blog(request):
    if request.method !='POST':
        form =Blogform()
    else:
        form = Blogform(data= request.POST)
        if form.is_valid():
            new_blog=form.save(commit=False)
            new_blog.owner=request.user
            new_blog.save()
            return redirect('blogs:blog',blog_id=new_blog.id)
    context={'form':form}
    return render(request, 'blogs/new_blog.html',context)

@login_required
def add_comment(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    comments=blog.comment_set.order_by('-date_added')
    if request.method != 'POST':
        form = Commentform()
    else :
        form = Commentform(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.blog=blog
            new_comment.owner=request.user
            new_comment.save()
            return redirect('blogs:blog',blog_id=blog.id)
    context={'blog':blog,'comments':comments,'form':form}    
    return render(request,'blogs/add_comment.html',context)

@login_required
def delete_comment(request,comment_id):
    comment=Comment.objects.get(id=comment_id)
    id=comment.blog.id
    check_user(request,comment.owner)
    comment.delete()
    return redirect('blogs:blog',blog_id=id)
    
@login_required
def edit_comment(request,comment_id):
    comment=Comment.objects.get(id=comment_id)
    blogid=comment.blog.id
    # blog=Blog.objects.get(id=blogid)
    check_user(request,comment.owner)
    if request.method != 'POST':
        form = Commentform(instance=comment)
    else :
        form = Commentform(instance=comment,data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('blogs:blog',blog_id=blogid)
    # comments=blog.comment_set.order_by('-date_added')    
    context={'comment':comment,'form':form}    
    return render(request,'blogs/edit_comment.html',context)

@login_required
def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    check_user(request,blog.owner)
    if request.method != 'POST':
        form = Blogform(instance=blog)
    else :
        form = Blogform(instance= blog,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog',blog_id=blog.id)
    context={'blog':blog,'form':form}
    return render (request,'blogs/edit_blog.html',context)    

@login_required
def delete_blog(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    check_user(request,blog.owner)
    blog.delete()
    return redirect('blogs:blogs')

def check_user(request,owner):
    if owner != request.user :
        raise Http404