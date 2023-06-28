from django.urls import path
from apps.web.views import account

urlpatterns = [
      path('', account.home, name="home"),
      path('login/', account.login),
      path('logout/', account.logout),
      path('auth/', account.auth),
]

app_name = 'web'
