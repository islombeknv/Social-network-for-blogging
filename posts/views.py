from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from posts.forms import PostModelForm, TagModelForm, CategoryModelForm
from posts.models import PostTagModel, CategoryModel, PostModel


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostModelForm

    def get_success_url(self):
        return reverse('blog:table-post')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.request.user.tags.all()
        context['categories'] = self.request.user.category.all()
        return context


class UpdatePostView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PostModel
    form_class = PostModelForm
    template_name = 'update_post.html'
    success_message = 'Post successfully updated'

    def get_success_url(self):
        return reverse('blog:table-post')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.request.user.tags.all()
        context['categories'] = self.request.user.category.all()
        return context


class PostDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PostModel
    success_url = reverse_lazy('list')
    success_message = "Post successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:table-post')


class PostTableView(LoginRequiredMixin, ListView):
    template_name = 'posttable.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = self.request.user.posts.order_by('-pk')

        if q:
            qs = self.request.user.posts.filter(title__icontains=q)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postcount'] = self.request.user.posts.count()

        return context


class TagCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tags.html'
    form_class = TagModelForm

    def get_success_url(self):
        return reverse('blog:tags-create')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q', '')

        context = super(TagCreateView, self).get_context_data(**kwargs)
        context['tags'] = self.request.user.tags.filter(title__icontains=q).order_by('-pk')
        context['tagscount'] = self.request.user.tags.count()
        return context


class TagUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = PostTagModel
    template_name = 'tags.html'
    form_class = TagModelForm
    success_message = 'Tag successfully updated'

    def get_success_url(self):
        return reverse('blog:tags-create')


class TagDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = PostTagModel
    success_url = reverse_lazy('list')
    success_message = "Tag successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:tags-create')


class CategoryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'category.html'
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse('blog:category')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q', '')
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['category'] = self.request.user.category.filter(title2__icontains=q).order_by('-pk')
        context['categorycount'] = self.request.user.category.count()

        return context


class CategoryDelateView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = CategoryModel
    success_url = reverse_lazy('list')
    success_message = "Category successfully deleted."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:category')


class CatUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = CategoryModel
    template_name = 'category.html'
    form_class = CategoryModelForm
    success_message = 'Category successfully updated'

    def get_success_url(self):
        return reverse('blog:category')
