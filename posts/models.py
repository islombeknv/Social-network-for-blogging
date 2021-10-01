from datetime import datetime

import pytz
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class CategoryModel(models.Model):
    title2 = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'), null=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE, related_name='category', verbose_name=_('user'), null=True)

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 1

    def __str__(self):
        return self.title2

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class PostTagModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'), null=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE, related_name='tags', verbose_name=_('user'), null=True)

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 1

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostModel(models.Model):
    title = models.CharField(max_length=512, verbose_name=_('title'))
    postinfo = models.TextField(max_length=150, verbose_name=_('postinfo'))
    image = models.ImageField(upload_to='posts', verbose_name=_('image'))
    banner = models.ImageField(upload_to='post_banners', verbose_name=_('banner'))
    content = RichTextUploadingField(verbose_name=_('content'))
    blog_views = models.IntegerField(default=0, null=True, blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE, related_name='posts', verbose_name=_('user'))

    tags = models.ManyToManyField(
        PostTagModel, related_name='posts', verbose_name=_('tags'))

    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products',
                                 verbose_name=_('category'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'), null=True)

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 7

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comments.order_by('-created_on')

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    post = models.ForeignKey(
        PostModel,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('comments')
    )

    name = models.CharField(max_length=80, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    comment = models.TextField(verbose_name=_('comment'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_('created_on'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
