from django.shortcuts import render, redirect
from item.models import item
from django.db.models import Q
from operator import attrgetter

def lost(request):
    it = item.objects.order_by('-item_date')
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        it = item.objects.filter(Q(item_name__icontains=query)|Q(item_description__icontains=query)).order_by('-item_date')
    context['it'] = it
    return render(request, 'lost.html',context)

def found(request):
    it = item.objects.order_by('-item_date')
    return render(request, 'found.html',{'it':it})

def home(request):
    return redirect('lost')
