from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def backend(request):
    return render(request, 'backend/index.html')
