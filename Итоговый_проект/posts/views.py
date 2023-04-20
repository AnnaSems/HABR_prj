from django.core.paginator import Paginator
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Post, User


def authorized_only(func):
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')
    return check_user


# Главная страницаs
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


# Дизайн
def design_page(request):
    posts = Post.objects.filter(category='Design').order_by('-pub_date')[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    template = 'posts/design.html'
    return render(request, template, context)


# Веб-разработка
def web_dev_page(request):
    posts = Post.objects.filter(
        category='Web').order_by('-pub_date')[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    template = 'posts/web_dev.html'
    return render(request, template, context)


# Мобильная разработка
def mob_dev_page(request):
    posts = Post.objects.filter(category='Mobile').order_by('-pub_date')[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    template = 'posts/mob_dev.html'
    return render(request, template, context)


# Маркетинг
def market_page(request):
    posts = Post.objects.filter(
        category='Marketing').order_by('-pub_date')[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    template = 'posts/market.html'
    return render(request, template, context)


def profile(request, username):
    author = get_object_or_404(User, username=username)
    latest = author.posts.all().order_by('-pub_date')
    paginator = Paginator(latest, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
        "author": author,
        'paginator': paginator
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post_pk = Post.objects.filter(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    author = post.author
    context = {
        'post_pk': post_pk,
        'author': author,
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def new_post(request):
    user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('homepage')
        return render(request, 'posts/new.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/new.html', {'form': form})
