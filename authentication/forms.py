from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser

# Using django's LogIn View
class LogInForm(AuthenticationForm):
     username = forms.CharField()
     password = forms.CharField()
     
     def save(self, commit=True):
          user = super(LogInForm, self).save(commit=False)
          user.username = self.cleaned_data['username']
          user.password = self.cleaned_data['password']
          
          if commit:
               user.save()
               
          return user
  
class RegisterForm(UserCreationForm):
     username = forms.CharField()
     email = forms.EmailField()
     password1 = forms.CharField()
     password2 = forms.CharField()
     
     def save(self, request, commit=True):
          user = super(RegisterForm, self).save(commit=False)
          user.email = self.cleaned_data['email'] # This sets the user's email using the value from self.cleaned_data, which contains the form's validated input data. In this case, it's pulling the email entered by the user.
          user.username = self.cleaned_data['username']
          
          # Hash the password before saving
          user.set_password(self.cleaned_data['password1'])
    
          if commit:
               user.save()
          
          # Log in the user after registration
          new_user = authenticate(username=user.username, password=self.cleaned_data['password1'])
          if new_user is not None:
               login(request, new_user)

          return user
     
     def clean_email(self):
          email = self.cleaned_data.get('email')
          if CustomUser.objects.filter(email=email).exists():
               raise forms.ValidationError("Email is already in use.")
          return email
     
     class Meta:
          model = CustomUser
          ordering = ('username',)
          fields = ('username', 'email', 'password1', 'password2')
          