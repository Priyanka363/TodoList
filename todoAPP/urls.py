from django.contrib import admin
from django.urls import path
from todoAPP.views import home,login,signup,todo_add

urlpatterns = [
  path('', home, name='index'),
  path('login/', login, name='login'),
  path('signup/', signup),
  path('todo_add/',todo_add),
]