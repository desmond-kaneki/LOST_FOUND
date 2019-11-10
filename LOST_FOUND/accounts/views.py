from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm, UserProfileForm, LoginForm
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = UserForm(data=request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.save()
            auth.login(request,user)
            return redirect('lost')
        else:
            return render(request,'accounts/signup.html',{'error':signup_form.errors, 'form':UserForm})
    elif request.user.is_authenticated:
        return redirect('lost')
    else:
        return render(request, 'accounts/signup.html',{'form':UserForm})

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = authenticate(username=login_form.cleaned_data['username'], password=login_form.cleaned_data['password'])
            if user is not None:
                auth.login(request,user)
                return redirect('lost')
            else:
                return render(request, 'accounts/login.html', {'error':'Incorrect username or password','login_form':LoginForm})
        else:
            return render(request, 'accounts/login.html', {'error':'Form data invalid!! Try again..','login_form':LoginForm})
    elif request.user.is_authenticated:
        return redirect('lost')
    else:
        return render(request, 'accounts/login.html', {'login_form':LoginForm})

@login_required
def user_logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('lost')

@login_required
def user_profile(request):
    return render(request, 'accounts/profile.html',{'user':request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile = profile_form.save()
            profile.save()
            return redirect('profile')
        else:
            return render(request, 'accounts/update_profile.html', {'form':UserProfileForm, 'error':profile_form.errors })
    else:
        return render(request, 'accounts/update_profile.html', {'form':UserProfileForm})
