from django.contrib import admin
from django.urls import path
from todoAPP.views import home,login,signup,todo_add,sign_out,todo_del,todo_status

urlpatterns = [
  path('', home, name='index'),
  path('login/', login, name='login'),
  path('signup/', signup),
  path('todo_add/',todo_add),
  path('logout/',sign_out),
  path('todo_del/<int:id>',todo_del),
  path('todo_status/<int:id>/<str:status>',todo_status),

]