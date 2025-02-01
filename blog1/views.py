from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def postview(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request,'home.html',context=context)

def postdetail(request,id):
    post = Post.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request,'post_detail.html',context=context)

def postcreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.author = request.user
            posts.save()
            return redirect('post_detail')
    else:
        form = PostForm()
    context = {
        'form':form
    }
    return render(request,'post_create.html',context=context)

def postedit(request,id):
    posts = get_object_or_404(Post,id=id)
    if request.user != posts.author and not request.user.is_staff:
        return redirect('post_view')
    
    if request.method == 'POST':
        form = PostForm(request.POST,instance=posts)
        if form.is_valid():
            form.save()
            return redirect('post_detail',id=posts.id)
    else:
        form = PostForm(instance=posts)
    context = {
        'form':form
    }
    return render(request,'post_edit.html',context=context)

def postdelete(request,id):
    post = get_object_or_404(Post,id=id)
    if request.user != post.author and not request.user.is_staff:
        return redirect('post_view')
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_view')
    
    context = {
        'post':post
    }
    return render(request,'post_delete.html',context=context)
    