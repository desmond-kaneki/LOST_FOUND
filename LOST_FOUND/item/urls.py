from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('new_item',views.new_item_view,name='new_item'),
]
