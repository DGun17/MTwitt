# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitt',
            name='date_twit',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
