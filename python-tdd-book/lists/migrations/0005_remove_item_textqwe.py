# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-10 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_textqwe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='textqwe',
        ),
    ]