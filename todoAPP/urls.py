from django.contrib import admin
from django.urls import path
from todoAPP.views import home,login,signup

urlpatterns = [
  path('', home, name='index'),
  path('login/', login, name='login'),
  path('signup/', signup),
]