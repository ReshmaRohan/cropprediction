# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-28 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20190328_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
    ]
