from django.shortcuts import render,redirect
from .models import Post
from .form import PostForm
from django.http import JsonResponse


def index(request):
    return render(request, 'main/index.html', {'title': 'Home Page'})


def about(request):
    return render(request, 'main/about.html', {'title': 'About company'})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {'title': 'Posts', 'posts': posts})


def post_create(request):
    err = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            err = 'Error on save Post'
    else:
        form = PostForm()
    context = {
        'form': form,
        'err': err,
    }
    return render(request, 'main/post_create.html', context=context)


def api_response(request):
    posts = Post.objects.all().values()
    posts_list = list(posts)
    return JsonResponse(posts_list, safe=False)
