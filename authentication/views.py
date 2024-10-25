from django.contrib.auth import logout as Logout
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required
def profile(request):
     user = request.user
     if request.method == 'POST':
          form = ProfileForm(request.POST, request.FILES, instance=user)
          if form.is_valid():
               form.save()
               return redirect('authentication:profile')
     else:
          form = ProfileForm(instance=user) 
     return render(request, 'authentication/profile.html', {'form': form})
     
     
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
     return redirect('/')


@login_required
def delete_acc(request):
     request.user.delete()
     logout(request)
     
     return redirect('authentication:login')