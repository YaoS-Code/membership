from django.urls import path
from apps.backend import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('signup', views.signup),

]

app_name = 'backend'
