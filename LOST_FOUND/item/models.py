from django.db import models
from django.contrib.auth.models import User

class item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=128,null=False)
    item_image = models.ImageField(upload_to='item_image/',blank=False,null=True)
    item_description = models.CharField(max_length=256,blank=False)
    item_date = models.DateField()
    item_status_choices = (('L','LOST'),('F','FOUND'))
    item_status = models.CharField(max_length=1,choices=item_status_choices)
    item_last_place_seen = models.CharField(max_length=256,blank=False)

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment_item = models.ForeignKey(item, on_delete=models.CASCADE, related_name='item_comments')
    commented_on = models.DateTimeField(auto_now_add = True)
    body = models.TextField()

    class Meta:
        ordering = ['-commented_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user)
