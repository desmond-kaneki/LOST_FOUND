from django.shortcuts import render
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import new_item
# Create your views here.

@login_required
def new_item_view(request):
    if request.method == 'POST':
        form = new_item(data=request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('lost')
        else:
            return render(request,'new_item.html',{'form':new_item,'error':'Form data invalid!! Try again..'})
    else:
        return render(request,'new_item.html',{'form':new_item})
