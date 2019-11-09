from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rollno = models.CharField(max_length=20,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True)

    def __str__(self):
        return self.user.username

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username
