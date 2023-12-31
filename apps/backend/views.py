from django.contrib import messages
from django.shortcuts import render, redirect
from apps.backend import models


def backend(request):
    return render(request, 'backend/index.html')


def index(request):
    return render(request, 'backend/index.html')


def login(request):
    return render(request, 'backend/login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']  # 从表单中获取用户名
        password = request.POST['password']  # 从表单中获取密码
        password2 = request.POST['password2']  # 从表单中获取密码

        if password != password2:
            messages.success(request, 'Wrong Username or Password. Please Try Again!')
            return redirect('backend:signup')

        user = models.UserInfo.objects.create(email=email, password=password)
        # Add success message
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('backend:login')  # Redirect to login page

    return render(request, 'backend/signup.html')