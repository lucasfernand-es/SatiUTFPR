# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sati', '0002_person_status2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edition',
            old_name='beginDate',
            new_name='begin_date',
        ),
        migrations.RenameField(
            model_name='edition',
            old_name='endDate',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='edition',
            old_name='status',
            new_name='is_active',
        ),
    ]