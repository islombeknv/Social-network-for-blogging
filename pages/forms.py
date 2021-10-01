
from django import forms

from posts.models import CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('name', 'email', 'comment')