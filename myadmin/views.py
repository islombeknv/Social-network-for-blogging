from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView
from online_users.models import OnlineUserActivity
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

from account.models import ProfileModel
from contacts.models import ContactModel
from myadmin.forms import RecommendPostForms
from posts.forms import PostModelForm, CategoryModelForm
from posts.models import PostModel, PostTagModel, CommentModel, CategoryModel

UserModel = get_user_model()


class AdminTemplateView(UserPassesTestMixin, TemplateView):
    template_name = 'admin_pages/index.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super(AdminTemplateView, self).get_context_data(**kwargs)
        context['users'] = User.objects.count()
        context['online_users'] = OnlineUserActivity.get_user_activities().count()
        context['post_count'] = PostModel.objects.count()
        context['tag_count'] = PostTagModel.objects.count()
        context['comments'] = CommentModel.objects.count()
        context['category'] = CategoryModel.objects.count()
        context['views'] = PostModel.objects.aggregate(Sum('blog_views'))['blog_views__sum']
        return context


class UsersListView(UserPassesTestMixin, ListView):
    template_name = 'admin_pages/users.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = ProfileModel.objects.order_by('-pk')
        if q:
            qs = qs.filter(fullname__icontains=q)
        return qs


class AdminPostTableView(UserPassesTestMixin, ListView):
    template_name = 'admin_pages/posts.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = PostModel.objects.order_by('-pk')

        if q:
            qs = qs.filter(title__icontains=q)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postcount'] = PostModel.objects.count()

        return context


class AdminUpdatePostView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    form_class = PostModelForm
    template_name = 'admin_pages/update_post.html'
    model = PostModel
    success_message = 'Post successfully updated'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_success_url(self):
        return reverse('myadmin:table-post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = PostTagModel.objects.all()
        context['categories'] = CategoryModel.objects.all()
        return context


class AdminPostDeleteView(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = PostModel
    success_url = reverse_lazy('list')
    success_message = "Post successfully deleted."

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('myadmin:table-post')


class AdminCategoryListView(UserPassesTestMixin, ListView):
    template_name = 'admin_pages/category.html'
    model = CategoryModel

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_queryset(self):
        qs = CategoryModel.objects.order_by('-pk')
        q = self.request.GET.get('q', '')
        if q:
            qs = qs.filter(title2__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorycount'] = CategoryModel.objects.count()

        return context


class AdminCategoryDelateView(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = CategoryModel
    success_url = reverse_lazy('list')
    success_message = "Category successfully deleted."

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('myadmin:category')


class AdminCatUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = CategoryModel
    template_name = 'admin_pages/category.html'
    form_class = CategoryModelForm
    success_message = 'Category successfully updated'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_success_url(self):
        return reverse('myadmin:category')


class AdminTagTableView(UserPassesTestMixin, ListView):
    template_name = 'admin_pages/tags.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = PostTagModel.objects.order_by('-pk')

        if q:
            qs = qs.filter(title__icontains=q)

        return qs


class UserRatingTemplateView(UserPassesTestMixin, TemplateView):
    template_name = 'admin_pages/rating.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = UserModel.objects.all()
        context['view'] = PostModel.objects.values('blog_views')
        return context


class AdminContactListView(UserPassesTestMixin, ListView):
    template_name = 'admin_pages/messages.html'
    queryset = ContactModel.objects.order_by('view')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


class AdminContactDetailView(UserPassesTestMixin, DetailView):
    model = ContactModel
    template_name = 'admin_pages/messages_detail.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.view = True
        obj.save()
        return obj


class OnlineUserView(TemplateView):
    template_name = 'admin_pages/online_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        starting_time = timezone.now() - timedelta(minutes=5)
        online = OnlineUserActivity.objects.values('user').filter(last_activity__gte=starting_time).order_by(
            '-last_activity')
        users = list()
        for user in online:
            user = user.get('user')
            users += UserModel.objects.filter(id=user)
        context['online_users'] = users
        return context


class RecommendedPostUpdateView(UpdateView):
    template_name = 'admin_pages/recommend.html'
    form_class = RecommendPostForms
    model = PostModel

    def get_success_url(self):
        return reverse('myadmin:table-post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.filter(id=31)
        return context


def export_date(request):
    workbook = Workbook()
    sheet = workbook.active
    i = 0
    for user in ProfileModel.objects.all():
        if i == 0:
            sheet.append(["USER ID", "FULLNAME", 'ADDRESS', 'POSITION'])
        sheet.append([user.id, user.fullname, user.address, user.position])
        i += 1

    return HttpResponse(
        save_virtual_workbook(workbook),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )