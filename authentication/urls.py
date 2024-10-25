from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html', authentication_form = AuthenticationForm), name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete_acc, name='delete_acc'),
]