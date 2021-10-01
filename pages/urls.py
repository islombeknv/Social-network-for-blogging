from django.urls import path

from pages.views import AboutTemplate, MyPostListView, HomePostListView, PostDetailView, CommentCreateView

app_name = 'pages'

urlpatterns = [
    path('', HomePostListView.as_view(), name='home'),
    path('about/', AboutTemplate.as_view(), name='view'),
    path('myposts/', MyPostListView.as_view(), name='myposts'),
    path('post/detail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment'),
]