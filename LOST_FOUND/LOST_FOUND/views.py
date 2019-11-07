from django.shortcuts import render

def lost(request):
    return render(request, 'lost.html')
def found(request):
    return render(request, 'found.html')