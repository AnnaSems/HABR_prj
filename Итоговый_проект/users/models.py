from django.db import models
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class UserRegisterForm(UserCreationForm):
    img = models.ImageField(upload_to='images/',
                            verbose_name="Загрузить картинку", blank=True)