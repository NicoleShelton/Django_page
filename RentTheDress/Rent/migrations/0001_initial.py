# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dress', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('image', models.URLField()),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
