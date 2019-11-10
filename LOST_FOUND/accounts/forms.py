from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        fields = ('first_name','last_name','email','username','password1','password2')
        model = get_user_model()

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['first_name'].label = 'First Name'
            self.fields['last_name'].label = 'Last Name'
            self.fields['username'].label = 'Username'
            self.fields['email'].label = 'Email Address'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('rollno','profile_pic')

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
