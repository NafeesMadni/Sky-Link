from django.contrib.auth import logout as Logout
from django.shortcuts import render, redirect
from .forms import LogInForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def profile(request):
     pass

def login(request):
     return render(request, 'authentication/login.html')

def register(request):
     if request.method == 'POST':
          form = RegisterForm(request.POST)
          if form.is_valid():
               user = form.save(request)
               
               return redirect('/')
     else:
          form = RegisterForm() 
     return render(request, 'authentication/register.html', {'form':form})

@login_required
def logout(request):
     Logout(request)
     messages.success(request, 'You have been successfully logged out.')
     return redirect('/')