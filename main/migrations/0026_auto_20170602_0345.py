# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 07:45
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20170601_2324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thesis',
            name='link',
        ),
        migrations.AddField(
            model_name='thesis',
            name='file',
            field=models.FileField(max_length=500, null=True, upload_to=b'', verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='institution',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='link',
            field=models.URLField(blank=True, default='', max_length=500, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='person',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Enlace Web Personal'),
        ),
        migrations.AlterField(
            model_name='service',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='subservice',
            name='link',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='Enlace'),
        ),
        migrations.AlterField(
            model_name='thesis',
            name='info',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Informacion'),
        ),
    ]
