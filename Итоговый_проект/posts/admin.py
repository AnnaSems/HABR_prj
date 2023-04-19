from django.contrib import admin
# Из модуля models импортируем модель Post
from . models import Post


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'header', 'pub_date',
                    'author', 'category')
    # Добавляем интерфейс для поиска по тзаголовку постов
    search_fields = ('header',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date', 'category')


admin.site.register(Post, PostAdmin)
