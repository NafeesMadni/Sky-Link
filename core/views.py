from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import CustomUser
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
     return render(request, 'core/home.html')

def contact(request):
     return render(request, 'core/contact.html')

def about(request):
     return render(request, 'core/about.html')



@login_required
def meeting(request):
     user = request.user
     return render(request, 'core/room.html', {'name': user.nickname}) 

# ! you can't access room.html coz it contains some private data so contact me at nmadni82@gmail.com 

@login_required
def join(request):
     if request.method == 'POST':
          link = request.POST['roomID']
          return redirect(link)
     return render(request, 'core/join.html')