# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # Редактирование профиля
    path('profile/<int:id>/edit', views.edit_profile, name='edit_profile'),
    # Просмотр записи
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # разделы меню
    path('design/', views.design_page, name='design_page'),
    path('web_dev/', views.web_dev_page, name='web_dev'),
    path('mob_dev/', views.mob_dev_page, name='mob_dev'),
    path('marketing/', views.market_page, name='market'),
    # Новый пост
    path('new/', views.new_post, name='new_post'),
    # Черновик
    path('draft_post/', views.draft_new_post, name='draft_post'),
    # Черновики пользователя
    path('draft_arcticle/<str:username>/',
         views.draft_article, name='draft_article'),
    # Редактирование черновика
    path('posts/<int:post_id>/post_edit/',
         views.edit_draft_article, name='draft_edit'),
    # удаление черновика
    path('post/delete/<int:post_id>/',
         views.hide_draft, name='draft_hide'),
    # редактирование поста
    path('posts/<int:post_id>/post_edit/',
         views.post_edit, name='post_edit'),
    # удаление поста
    path('posts/delete/<int:post_id>/',
         views.hide_post, name='post_hide'),
    # комментарии
    path('posts/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    # лайки
    path('posts/<int:post_id>/like/', views.like_dislike, name="post_like"),
    path('posts/<int:post_id>/<int:comment_id>/like/',
         views.like_to_comment, name="comment_like"),
    # поиск
    path('search/', views.search_page, name="search"),
    # выборка по релевантности
    # path('search/req/', views.search_relevant, name="search_rel"),
]
