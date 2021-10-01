from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from posts.models import PostModel, PostTagModel, CategoryModel


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = PostModel
        exclude = [
            'user',
            'created_at',
        ]


class TagModelForm(forms.ModelForm):
    class Meta:
        model = PostTagModel
        fields = ['title']


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['title2']
