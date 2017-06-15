# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('floybd', '0013_auto_20170605_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='agency_id',
            new_name='agency',
        ),
        migrations.RenameField(
            model_name='stop_time',
            old_name='trip_id',
            new_name='trip',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='route_id',
            new_name='route',
        ),
        migrations.RemoveField(
            model_name='stop_time',
            name='stop_id',
        ),
        migrations.AddField(
            model_name='calendar_date',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stop_time',
            name='stop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='floybd.Stop'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='dynamic_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agency',
            name='agency_timezone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='calendar_date',
            name='service_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='stop_time',
            name='timepoint',
            field=models.IntegerField(blank=True, choices=[(0, 'Times are considered approximate'), (1, 'Times are considered exact')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='service_id',
            field=models.CharField(max_length=200),
        ),
    ]