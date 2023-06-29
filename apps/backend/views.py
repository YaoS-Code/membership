from django.http import HttpResponse
from django.shortcuts import render
from apps.backend import models


def backend(request):
    return render(request, 'backend/index.html')


def index(request):
    obj1 = models.Membership.objects.create(level=0, discount=0.80, credit=10000, note="Diamond Membership")
    obj2 = models.Membership.objects.create(level=1, discount=0.90, credit=5000, note="Gold Membership")
    obj3 = models.Membership.objects.create(level=2, discount=0.80, credit=1000, note="Regular Membership")
    print(obj1)
    print(obj2)
    print(obj3)
    return HttpResponse()


def login(request):
    return render(request, 'backend/login.html')

def signup(request):
    return render(request, 'backend/signup.html')
