from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, DeleteView,
    UpdateView
)

from .models import Post

posts = [
    {
        'author': 'John Doe',
        'title': 'First Blog Post',
        'content': 'The very first blog post',
        'date_posted': 'August 8, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Blog Post',
        'content': 'The second blog post',
        'date_posted': 'August 9, 2020'
    },
]


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # <model>_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']  # <model>_form.html

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

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')


def individual_posts(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse('<h1>The Blog Post</h1>'
                        '<p1>Hi, this is where an individual post will be.</p1>')


def comments(request):
    return HttpResponse('<div>'
                        '<h1>ABOUT US</h1>'
                        '<h3>'
                        'Ade.com is a website just W3 schools We are just like W3 schools <br>'
                        'We basically provide examples and prototypes for people who do not have full idea of HTML and CSS<br>'
                        'We provide introductory examples to learn, such that you can use the Inspect element option to view the source code which is basic'
                        '</h3>'
                        '</div>')  # Create your views here.

# Create your views here.
