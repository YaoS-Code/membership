from django.urls import path
from apps.backend import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]


app_name = 'backend'
