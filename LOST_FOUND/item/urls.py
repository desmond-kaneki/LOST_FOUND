from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('new_item/', views.new_item_view, name='new_item'),
    path('details/<int:item_id>', views.item_details, name='details'),
    path('delete/<int:item_id>',views.delete_item, name='delete'),
]
