# Generated by Django 2.2.1 on 2019-11-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_auto_20191126_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(blank=True, default='/item_image/default.png', null=True, upload_to='item_image/'),
        ),
    ]
