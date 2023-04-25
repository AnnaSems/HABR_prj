from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    CHOICES = (
        ("Design", "Дизайн"),
        ("Web", "Веб-разработка"),
        ("Mobile", "Мобильная разработка"),
        ("Marketing", "Маркетинг"),
    )

    header = models.TextField(max_length=60, verbose_name="Заголовок статьи")
    text = models.TextField(verbose_name="Текст статьи")
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    img = models.ImageField(upload_to='images/',
                            verbose_name="Загрузить картинку", blank=True)
    category = models.CharField(
        max_length=150, choices=CHOICES, null=True, blank=True, verbose_name="Выберите категорию")
    likes = models.ManyToManyField(User, related_name='like')

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    class Meta:
        db_table = "comments"
        ordering = ('created',)

    text = models.TextField(max_length=70, verbose_name="Комментарий")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    article = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.article)
