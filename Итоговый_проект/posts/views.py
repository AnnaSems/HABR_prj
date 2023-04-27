from django.core.paginator import Paginator
from .forms import PostForm, CommentForm
from users.forms import UserForm, UpdateForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.db.models import Max, Q
from django.urls import reverse
from . models import Post, Comment
from users.models import User


# Главная страницаs
def index(request):
    posts = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    max_rate_author = Post.objects.all().order_by('-likes')[:10]
    context = {
        'page_obj': page_obj,
        'max_rate': max_rate_author,
    }
    return render(request, 'posts/index.html', context)


# Дизайн
def design_page(request):
    posts = Post.objects.filter(category='Design').order_by('-pub_date')[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    max_rate_author = Post.objects.all().order_by('-likes')[:10]
    context = {
        'page_obj': page_obj,
        'max_rate': max_rate_author,
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
    max_rate_author = Post.objects.all().order_by('-likes')[:10]
    context = {
        'page_obj': page_obj,
        'max_rate': max_rate_author,
    }
    template = 'posts/web_dev.html'
    return render(request, template, context)


# Мобильная разработка
def mob_dev_page(request):
    posts = Post.objects.filter(category='Mobile').order_by('-pub_date')[:10]
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    max_rate_author = Post.objects.all().order_by('-likes')[:10]
    context = {
        'page_obj': page_obj,
        'max_rate': max_rate_author,
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
    max_rate_author = Post.objects.all().order_by('-likes')[:10]
    context = {
        'page_obj': page_obj,
        'max_rate': max_rate_author,
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
        'paginator': paginator,
    }
    return render(request, 'posts/profile.html', context)


@login_required
def edit_profile(request, id):
    author = get_object_or_404(User, pk=id)
    if author != request.user:
        return redirect('profile', username=author.username)

    form = UpdateForm(
        request.POST or None,
        files=request.FILES or None,
        instance=author
    )
    if form.is_valid():
        form.save()
        return redirect('profile', username=author.username)
    context = {
        'user': author,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'posts/profile_edit.html', context)


def post_detail(request, post_id):
    post_pk = Post.objects.filter(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    author = post.author
    comment_form = CommentForm(request.POST or None)
    all_comments = Comment.objects.filter(
        article=post_id).order_by('-created')
    context = {
        'post_pk': post_pk,
        'author': author,
        'post': post,
        'comment_form': comment_form,
        'all_comments': all_comments
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def new_post(request):
    user = request.user
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('homepage')
        return render(request, 'posts/new.html', {'form': form})
    form = PostForm()
    return render(request, 'posts/new.html', {'form': form})


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        return redirect('post_detail', post_id=post_id)

    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
    )
    if form.is_valid():
        form.save()
        return redirect('post_detail', post_id=post_id)
    context = {
        'post': post,
        'form': form,
        'is_edit': True,
    }
    return render(request, 'posts/new.html', context)


@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.article = post
        comment.save()
    return redirect('post_detail', post_id=post_id)


@login_required
def like_dislike(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post_detail', post_id=post_id)


@login_required
def like_to_comment(request, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return redirect('post_detail', post_id=post_id)


def search_page(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = Post.objects.filter(
            Q(header__icontains=search_post) & Q(text__icontains=search_post))
        posts_rate = Post.objects.filter(
            Q(header__icontains=search_post) & Q(text__icontains=search_post)).order_by('-likes')
        posts_pub_date = Post.objects.filter(Q(header__icontains=search_post) & Q(
            text__icontains=search_post)).order_by('-pub_date')
    else:
        return render(request, 'posts/search.html')

    return render(request, 'posts/search.html', {"posts": posts, 'posts_rate': posts_rate,
                                                 'posts_pub_date': posts_pub_date})


# def search_relevant(request, req):
#     search_post = request.GET.get('req')
#     posts = Post.objects.filter(
#         Q(header__icontains=search_post) & Q(text__icontains=search_post))
#     return render(request, 'posts/search.html', {"posts": posts,
#                                                  'req': req})

# def search_rate(request, req):
#     posts = Post.objects.filter(Q(header__icontains=search_post) & Q(text__icontains=search_post)).order_by('-pub_date')
#     return render(request, 'posts/search.html', {"posts": posts})

# def search_pub_date(request, req):
#     posts = Post.objects.filter(Q(header__icontains=search_post) & Q(text__icontains=search_post)).order_by('likes')
#     return render(request, 'posts/search.html', {"posts": posts})
