from django.shortcuts import render
from item.models import item

def lost(request):
    it = item.objects
    return render(request, 'lost.html',{'it':it})

def found(request):
    it = item.objects
    return render(request, 'found.html',{'it':it})