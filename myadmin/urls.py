from django.urls import path

from myadmin.views import AdminTemplateView, UsersListView, AdminPostTableView, AdminUpdatePostView, \
    AdminPostDeleteView, AdminCategoryListView, AdminCategoryDelateView, AdminCatUpdateView, AdminTagTableView, \
    UserRatingTemplateView, AdminContactListView, AdminContactDetailView, OnlineUserView, RecommendedPostUpdateView, \
    export_date

app_name = 'myadmin'

urlpatterns = [
    path('', AdminTemplateView.as_view(), name='home'),
    path('users/', UsersListView.as_view(), name='users'),
    path('admin/post/table', AdminPostTableView.as_view(), name='table-post'),
    path('update/post/<int:pk>', AdminUpdatePostView.as_view(), name='post-update'),

    path('admin/delete/post/<int:pk>/', AdminPostDeleteView.as_view(), name='post-delete'),
    path('admin/category', AdminCategoryListView.as_view(), name='category'),
    path('delate/category/<int:pk>/', AdminCategoryDelateView.as_view(), name='category-del'),
    path('update/category/<int:pk>/', AdminCatUpdateView.as_view(), name='category-update'),

    path('admin/tag/table', AdminTagTableView.as_view(), name='tag'),
    path('admin/users/rating', UserRatingTemplateView.as_view(), name='rating'),
    path('admin/contact/messages/', AdminContactListView.as_view(), name='messages'),
    path('admin/messages/detail/<int:pk>/', AdminContactDetailView.as_view(), name='messages-detail'),

    path('recommended/post/<int:pk>', RecommendedPostUpdateView.as_view(), name='recommended'),
    path('admin/online-users/', OnlineUserView.as_view(), name='online-users'),
    path('import/', export_date, name='excel'),

]
