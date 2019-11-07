from django.db import models

class item(models.Model):
    item_name = models.CharField(max_length=128,null=False)
    item_image = models.ImageField(upload_to='item_image/',blank=False,null=True)
    item_description = models.CharField(max_length=256,blank=False)
    item_date = models.DateField()
    item_status_choices = (('L','LOST'),('F','FOUND'))
    item_status = models.CharField(max_length=1,choices=item_status_choices)
    item_user = models.CharField(max_length=128,blank=False,null=False)
    item_last_place_seen = models.CharField(max_length=256,blank=False)