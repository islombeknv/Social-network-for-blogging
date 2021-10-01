from django.urls import path

from posts.views import PostCreateView, TagCreateView, \
    CategoryCreateView, TagUpdateView, TagDeleteView, \
    CategoryDelateView, CatUpdateView, PostTableView, PostDeleteView, UpdatePostView

app_name = 'blog'

urlpatterns = [
    path('create/post/', PostCreateView.as_view(), name='create'),
    path('update/post/<int:pk>', UpdatePostView.as_view(), name='post-update'),
    path('delete/post/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/table', PostTableView.as_view(), name='table-post'),

    path('create/category/', CategoryCreateView.as_view(), name='category'),
    path('delate/category/<int:pk>/', CategoryDelateView.as_view(), name='category-del'),
    path('update/category/<int:pk>/', CatUpdateView.as_view(), name='category-update'),

    path('create/tag/', TagCreateView.as_view(), name='tags-create'),
    path('update/tag/<int:pk>/', TagUpdateView.as_view(), name='tag-update'),
    path('delete/<int:pk>/', TagDeleteView.as_view(), name='tags-delete'),
]
