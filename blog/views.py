from django.http import HttpResponse
from django.shortcuts import render

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
