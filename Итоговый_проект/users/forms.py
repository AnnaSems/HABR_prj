from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User


#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):

        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'age', 'img', 'description')


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'age', 'img', 'description']
