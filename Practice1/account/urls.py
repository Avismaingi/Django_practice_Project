from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('info/', views.info, name='info'),
]
