from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Добавили поле image в форму
        fields = ('header', 'text', 'img', 'category')


class CommentForm(forms.ModelForm):
    # content = forms.CharField(label="", widget=forms.Textarea(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Комментарий',
    #         'rows': 1,
    #         'cols': 20
    #     }))

    class Meta:
        model = Comment
        fields = ['text']
