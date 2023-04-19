from django.shortcuts import render
from . models import Post


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


# Дизайн
def design_page(request):
    posts = Post.objects.filter(category='Design').order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    template = 'posts/design.html'
    return render(request, template, context)


# Веб-разработка
def web_dev_page(request):
    posts = Post.objects.filter(
        category='Web').order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    template = 'posts/web_dev.html'
    return render(request, template, context)


# Мобильная разработка
def mob_dev_page(request):
    posts = Post.objects.filter(category='Mobile').order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    template = 'posts/mob_dev.html'
    return render(request, template, context)


# Маркетинг
def market_page(request):
    posts = Post.objects.filter(
        category='Marketing').order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    template = 'posts/market.html'
    return render(request, template, context)
