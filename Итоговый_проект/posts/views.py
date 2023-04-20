from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Post


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
