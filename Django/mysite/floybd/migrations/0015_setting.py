# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floybd', '0014_auto_20170608_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=10)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
    ]
