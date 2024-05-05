
# accounts/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Page, Blog

def home(request):
    categories = Category.objects.all()
    pages = Page.objects.filter(is_published=True)
    posts = Blog.objects.filter(status=1)
    return render(request, 'home.html', {'categories': categories, 'pages': pages, 'posts': posts})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def post(request):
    posts = Blog.objects.filter(status=1)
    return render(request, 'post.html', {'posts': posts})

def pencatatan(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'pencatatan.html', {'pencatatan': pencatatan})

def contact(request):
    posts = Blog.objects.filter(status=1)
    return render(request, 'contact.html', {'contact': contact})

def login(request):
    posts = Blog.objects.filter(status=1)
    return render(request, 'login.html', {'login': login})