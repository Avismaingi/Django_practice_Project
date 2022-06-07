from multiprocessing import context
from django.shortcuts import render, HttpResponse

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.


def home(request):
     return render(request, "home.html")

def user_login(request):
     if request.method=='POST':
          email=request.POST.get('email')
          password=request.POST.get('password')
          user=authenticate(email=email, password=password)
          print(email)
          print(password)
          if user is not None:
               login(request,user)
               return render(request, 'info.html')
          else:
               return render(request, 'login.html')

     return render(request, "login.html")

def register(request):
     if request.method=='POST':
          email=request.POST.get('email')
          username=request.POST.get('username')
          password=request.POST.get('password')
          first_name=request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          myuser=User.objects.create_user(email,username,password,first_name,last_name)
          myuser.save()
          render(request,info.html)
     return render(request, "register.html")

def info(request):
     return render(request, "info.html")