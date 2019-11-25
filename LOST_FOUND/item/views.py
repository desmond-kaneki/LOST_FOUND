from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import new_item, CommentForm
from .models import item, comments
from accounts.views import my_items
# Create your views here.

@login_required
def new_item_view(request):
    if request.method == 'POST':
        form = new_item(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('lost')
        else:
            return render(request,'new_item.html',{'form':new_item,'error':form.errors})
    else:
        return render(request,'new_item.html',{'form':new_item})



def item_details(request, item_id):
    Item = get_object_or_404(item, pk=item_id)
    if request.method == 'POST':
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.user = request.user
            comment.comment_item = Item
            comment.save()
    return render(request, 'details.html', {'item':Item, 'comments':Item.item_comments.all(), 'form': CommentForm})


@login_required
def delete_item(request, item_id):
    it = get_object_or_404(item, pk=item_id)
    if it.user == request.user:
        it.delete()
    return redirect(my_items)