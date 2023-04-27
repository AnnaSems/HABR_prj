from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(
        max_length=25, verbose_name="ник пользователя", unique=True)
    first_name = models.CharField(max_length=15, verbose_name="Имя")
    last_name = models.CharField(max_length=20, verbose_name="Фамилия")
    email = models.EmailField(max_length=30, verbose_name="Почта", unique=True)
    img = models.ImageField(upload_to='images/',
                            verbose_name="Загрузить картинку", blank=True, default='images/avatardefault.jpeg')
    age = models.IntegerField(verbose_name='Возраст', blank=True, null=True)
    description = models.TextField(
        max_length=300, verbose_name='Краткое описание', blank=True)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
