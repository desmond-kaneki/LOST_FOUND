from django import forms
from .models import item, comments

class new_item(forms.ModelForm):
    class Meta:
        model = item
        fields = ('item_name','item_image','item_description','item_date','item_status','item_last_place_seen')

class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ('body',)
        labels = {
                    'body':'Write a comment',
        }
