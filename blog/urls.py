from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogList, name='blog-home'),
    path('about', views.about),
    path('blog', views.blog_page),
]
