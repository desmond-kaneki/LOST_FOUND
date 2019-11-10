from django.shortcuts import render, redirect
from item.models import item

def lost(request):
    it = item.objects.order_by('-item_date')
    return render(request, 'lost.html',{'it':it})

def found(request):
    it = item.objects.order_by('-item_date')
    return render(request, 'found.html',{'it':it})

def home(request):
    return redirect('lost')
