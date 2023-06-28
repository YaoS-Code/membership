from django.urls import path
from apps.backend import views

urlpatterns = [
    path('', views.backend)
]

app_name = 'backend'
