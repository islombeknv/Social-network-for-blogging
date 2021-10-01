from django import forms

from posts.models import PostModel


class RecommendPostForms(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['category']