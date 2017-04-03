# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-03 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dress',
            old_name='dress',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='dress',
            name='image',
        ),
        migrations.AddField(
            model_name='dress',
            name='img',
            field=models.CharField(default='img.jpg', max_length=100),
            preserve_default=False,
        ),
    ]
