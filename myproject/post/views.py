from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SubscribeForm
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('title')[:10]
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

def post_create(request):
    return HttpResponse("Create post")


def post_update(request, post_id):
    return HttpResponse(f"Update post id:{post_id}")


def post_delete(request, post_id):
    return HttpResponse(f"Delete post id:{post_id}")

def post_favorites(request, post_id):

    return HttpResponse(f"Favorites post id:{post_id}")