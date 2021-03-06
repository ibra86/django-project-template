# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-07 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Surname')),
                ('middle_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Patronimic')),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Photo')),
                ('ticket', models.CharField(max_length=256, verbose_name='Tickets')),
                ('notes', models.TextField(blank=True, verbose_name='Additional notes')),
            ],
        ),
    ]
