from django.shortcuts import render
from . import forms
from .forms import new_item
# Create your views here.

def new_item_view(request):
    form = forms.new_item()
    return render(request,'new_item.html',{'form':form})