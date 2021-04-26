from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as login_acc, logout
from django.views.decorators.csrf import csrf_protect
from todoAPP.forms import add_todo
from todoAPP.models import List 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
  if request.user.is_authenticated:
    user=request.user
    form=add_todo()
    data_todo=List.objects.filter(user=user).order_by('precedence')
    count=List.objects.filter(status='P').count()
    context={'form':form,'data_todo':data_todo,'count':count}
    return render(request, 'home.html',context=context) 

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

@login_required(login_url='login')
def todo_add(request):
  if request.user.is_authenticated:
    form=add_todo(request.POST)
    context={'form':form}
    if form.is_valid():
      todo=form.save(commit=False)
      todo.user=request.user
      todo.save()
      return redirect('index')
    else:
      return render(request, 'AddTodo.html', context=context)

@login_required(login_url='login')
def sign_out(request):
  logout(request)
  return redirect('login')

def todo_del(request ,id):
  List.objects.get(pk=id).delete()
  return redirect('index')

def todo_status(request,id,status):
  todo=List.objects.get(pk=id)
  todo.status=status
  todo.save()
  return redirect('index')
