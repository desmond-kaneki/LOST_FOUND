from django import forms

class new_item(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea)
    date = forms.DateField()
    status_choices = (('L','LOST'),('F','FOUND'))
    status = forms.ChoiceField(choices=status_choices)
    user = forms.CharField()
    last_seen_place = forms.CharField()
