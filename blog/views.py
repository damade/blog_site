from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<div>'
						'<h1>Hello, welcome to the index page</h1>'
						'<div>')

def home(request):
	return HttpResponse('<div>'
						'<h1>Blog Home</h1>'
						'<div>')

def about(request):
	return HttpResponse('<div>'
						'<h1>Blog About Page</h1>'
						'<div>')

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
