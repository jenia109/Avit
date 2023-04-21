from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import SubscribeForm, PostForm
from .models import Post


def index(request):
    posts = Post.objects.all().annotate(count_favorites=Count('favorites')).order_by('count_favorites')[:10]
    context = {
        "header": "All posts",
        "posts": posts,
    }
    return render(request, 'post/index.html', context)


def feed(request):
    return HttpResponse("Лента объявлений")


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        header = f"Post: {post.title}"
    except Post.DoesNotExist:
        post = None
        header = "No post."
    context = {
        "header": header,
        "post": post,
    }
    return render(request, 'post/detail.html', context)

def subscribe_view(request):
    if request.method == 'Post':
        print(request.Post)
        form = SubscribeForm(request.Post)
        if form.is_valid():
            print(form.cleaned_data.get('your_name'), form.cleaned_data.get('email'))
            return redirect('post:subscribe')

    else:
        form = SubscribeForm()

    context ={
        "header": "Subscribe",
        'form': form
    }

    return render(request, 'post/subscribe.html', context)

@login_required
def post_create(request):
    if request.method =='GET':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post.get_absolute_urls())

    context = {
        "header": "Create post",
        'form': form
    }

    return render(request, 'post/post_create.html', context)

def post_update(request, post_id):
    return HttpResponse(f"Update post id:{post_id}")


def post_delete(request, post_id):
    return HttpResponse(f"Delete post id:{post_id}")

def post_favorites(request, post_id):
    return HttpResponse(f"favorites post id: {post_id}")