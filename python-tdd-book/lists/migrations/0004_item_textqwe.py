# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_remove_item_textqjwejqwoie'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='textqwe',
            field=models.TextField(default=''),
        ),
    ]
