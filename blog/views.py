from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    context = {'message': "hello"}
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html")


def blog_page(request):
    context = {'content': "i m blog and i m just happy that i exist", 'by': "sakthi"}
    return render(request, "blogTemplate.html", context)


def blogList(request):
    context = {
        'posts': Post.objects.all(),
        'title': "Blog page"
    }
    return render(request,'blogList.html',context)
