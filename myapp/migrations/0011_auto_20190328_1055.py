# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-28 05:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20190328_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]