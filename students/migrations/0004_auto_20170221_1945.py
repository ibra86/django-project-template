# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-21 18:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_group_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='student_group',
        ),
        migrations.AddField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='Group'),
        ),
    ]
