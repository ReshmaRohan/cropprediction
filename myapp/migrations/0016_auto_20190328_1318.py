# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-28 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20190328_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
