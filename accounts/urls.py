# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('post/', views.post, name='post'),
    path('financial/', views.financial, name='financial'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),

]
