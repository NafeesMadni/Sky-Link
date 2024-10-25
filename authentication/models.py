import os
from django.db import models
from django.contrib.auth.models import AbstractUser

def get_default_image_path():
    return os.path.join('user_dp', 'default.png')

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,)
    dp = models.ImageField(upload_to='user_dp/', default=get_default_image_path,)
    nickname = models.CharField(default='James Doe', max_length=15)
    acc_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)