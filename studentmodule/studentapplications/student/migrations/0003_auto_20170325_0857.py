# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20170325_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentadditionalinfo',
            name='student_id',
            field=models.CharField(max_length=20),
        ),
    ]