# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-20 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_ticketsale'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_tickets',
            field=models.BooleanField(default=False),
        ),
    ]
