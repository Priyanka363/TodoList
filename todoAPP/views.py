from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as login_acc
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def home(request):
  #print('Hello')
  return render(request, 'home.html')

@csrf_protect
def login(request):
  if request.method=='GET':
    form=AuthenticationForm()
    context={
      'form':form
    }
    return render(request,'login.html',context=context)

  else:
    form=AuthenticationForm(data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get('username')
      password=form.cleaned_data.get('password')
      user=authenticate(username=username, password=password)
      if user is not None:
        login_acc(request,user)
        return redirect('index')
    else:
      context={
        'form':form
      }
      return render(request,'login.html',context=context)

@csrf_protect
def signup(request):
  if request.method=='GET':
    form=UserCreationForm()
    context= {
      'form':form
    }
    return render(request,'signup.html',context=context)
  
  else:
    form=UserCreationForm(request.POST)
    context={
      'form':form
    }
    if form.is_valid():
      user=form.save()
      if user is not None:
        return redirect('login')
    else:
      return render(request, 'signup.html', context=context)