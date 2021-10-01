from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.urls import reverse
from django.views.generic import UpdateView

from account.forms import AccountModelForm
from account.models import ProfileModel
from posts.models import CommentModel


class AccountUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = ProfileModel
    template_name = 'my_account.html'
    form_class = AccountModelForm
    success_message = 'Profile successfully updated'

    def get_object(self, queryset=None):
        profile, _ = ProfileModel.objects.get_or_create(user=self.request.user)
        return profile

    def get_success_url(self):
        return reverse('account:update')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_count'] = self.request.user.tags.count()
        context['categorycount'] = self.request.user.category.count()
        context['blog_views'] = self.request.user.posts.aggregate(Sum('blog_views'))['blog_views__sum']
        context['comments'] = CommentModel.objects.filter(post__in=self.request.user.posts.all()).count()
        context['post_count'] = self.request.user.posts.count()
        context['my_profile'] = ProfileModel.objects.filter(
            user=self.request.user).values('image', 'fullname', 'position', 'address')

        return context
