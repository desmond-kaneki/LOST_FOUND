# Generated by Django 2.2.6 on 2019-11-25 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-commented_on']},
        ),
    ]
