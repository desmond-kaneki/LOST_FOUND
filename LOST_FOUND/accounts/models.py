from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    rollno = models.CharField(max_length=20,blank=True)
    profile_pic = models.ImageField(default='profile_pics/default_pic.png',upload_to='profile_pics/',blank=True)

    def __str__(self):
        return self.user.username

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username

@receiver(post_save, sender='auth.User')
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.save()
