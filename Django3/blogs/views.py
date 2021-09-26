from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
# Create your views here.

def index(request):
    """Strona główna wyświetlająca posty, w kolejności odwrotnie chronologicznej"""

    lastPost = BlogPost.objects.last()
    lastPost_id  = lastPost.id
    posts = BlogPost.objects.exclude(id=lastPost_id).order_by('-date_added')
    context = {'posts': posts, 'last': lastPost}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Strona z formularzem pozwalająca na dodanie posta"""
    
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Strona z formularzem pozwalająca na edycję posta"""

    post = BlogPost.objects.get(id=post_id)

    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'post':post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


