# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-12 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import mylinks.methods


class Migration(migrations.Migration):

    dependencies = [
        ('mylinks', '0002_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(db_index=True, max_length=200, unique=True, validators=[mylinks.methods.is_ascii], verbose_name='Link URL'),
        ),
    ]
