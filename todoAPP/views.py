from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
  #print('Hello')
  return render(request, 'home.html')

def login(request):
  return render(request,'login.html')

def signup(request):
  frm=UserCreationForm()
  context= {
    'form':frm
  }
  return render(request,'signup.html',context=context)