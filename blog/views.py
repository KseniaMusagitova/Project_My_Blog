
from django.contrib.auth.models import User, Post
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib import messages


from .forms import CommentForm
from .models import Post, Comment


# def home(request):
#     context = {'posts_for_html': Post.objects.all}
#     return render(request, 'blog/home.html', context)


class SuccessMessage:
    @property
    def success_message(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def get_succes_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/home.html'
    context_object_name = 'posts_for_html'
    ordering = ['-date_posted'] # сортировка по дате, самые новые будут на верху


class UserListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts_for_html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(SuccessMessage, FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    success_message = 'Комментарий успешно создан!'

    def get_success_url(self, **kwargs):
        return reverse_lazy('post-detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form() # в переменную в form занесла ту форму, которую отправили (запрос)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class LatestPostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = 'blog/latest.html'
    context_object_name = 'posts_for_html'
    ordering = ['-date_posted']


