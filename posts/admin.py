from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from posts.models import CategoryModel, PostModel, PostTagModel, CommentModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title2', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title2']


@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    list_filter = ['user', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['user', 'tags']
    #
    # class Media:
    #     js = (
    #         'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
    #         'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
    #         'modeltranslation/js/tabbed_translation_fields.js',
    #     )
    #     css = {
    #         'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    #     }


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_on']
    list_filter = ['created_on']
    search_fields = ['name', 'email']
