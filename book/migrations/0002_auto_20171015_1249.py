# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='author', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
