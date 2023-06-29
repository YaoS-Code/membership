from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'web/index.html')


def login(request):
    context = {
        'name': 'Yao Song',
        'password': '1216',
        'mylist': [
            {'id': 1, 'name': 'Yao', 'age': '39'},
            {'id': 2, 'name': 'Xin', 'age': '37'},
            {'id': 3, 'name': 'Hubery', 'age': '6'},
        ],

    }
    return render(request, 'web/index.html', context)


def logout(request):
    return HttpResponse("Logout Page")


def auth(request):
    url = reverse("web:login")
    return redirect(url)
