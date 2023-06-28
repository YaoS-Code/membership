from django.urls import path
from apps.api.views import apiviews

urlpatterns = [
    path('', apiviews.home)
]

app_name = 'api'
