# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-02 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
