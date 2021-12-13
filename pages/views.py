from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from pages.forms import CommentForm
from posts.models import PostModel


class AboutTemplate(TemplateView):
    template_name = 'about.html'


class MyPostListView(LoginRequiredMixin, ListView):
    template_name = 'my_post.html'

    def get_queryset(self):
        qs = self.request.user.posts.order_by('-pk')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('cat')
        if q:
            qs = qs.filter(title__icontains=q)

        elif cat:
            qs = qs.filter(category__title2__icontains=cat)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.request.user.category.all()
        return context


class HomePostListView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = sorted(PostModel.objects.all()[:4], key=lambda i: i.blog_views, reverse=True)
        context['recommended_posts'] = PostModel.objects.filter(category_id=31)

        return context


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'news-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object.category
        context['latest_news'] = PostModel.objects.order_by('-pk')[:4]
        context['related_posts'] = PostModel.objects.filter(category=self.object.category).exclude(
            pk=self.object.pk)

        return context

    def get_object(self):
        obj = super().get_object()
        obj.blog_views += 1
        obj.save()
        return obj


class CommentCreateView(CreateView):
    template_name = 'news-details.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pages:post_detail', kwargs={'pk': self.kwargs.get('pk')})
