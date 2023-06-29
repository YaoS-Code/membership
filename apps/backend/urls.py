from django.urls import path
from apps.backend import views

urlpatterns = [
    path('', views.index)

]

app_name = 'backend'
