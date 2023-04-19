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
        related_name='posts'
    ),
    img = models.ImageField(upload_to='images/',
                            verbose_name="Загрузить картинку")
    category = models.CharField(
        max_length=150, choices=CHOICES, null=True, blank=True)
    # like = models.ForeignKey(Like,)
    # comment = models.ForeignKey(Comment,)

    def __str__(self) -> str:
        return self.header
