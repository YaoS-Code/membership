from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'api/index.html')

