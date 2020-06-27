from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('index/', views.index, name='index'),
    path('post/', views.individual_posts, name='individual_posts'),
    path('comments/', views.comments, name='comments'),
    # path('contact/', views.contact, name='Contact')
]
