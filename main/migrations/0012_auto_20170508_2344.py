# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-09 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_datacenter_institution_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='title',
            new_name='name',
        ),
    ]
