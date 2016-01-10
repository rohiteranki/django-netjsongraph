# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django_netjsongraph.models.topology


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsongraph', '0002_topology_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='topology',
            name='key',
            field=models.CharField(blank=True, default=django_netjsongraph.models.topology.get_random_key, help_text='key needed to update topology from nodes (RECEIVE strategy)', max_length=64, verbose_name='key'),
        ),
        migrations.AddField(
            model_name='topology',
            name='strategy',
            field=models.CharField(choices=[('fetch', 'FETCH'), ('receive', 'RECEIVE')], db_index=True, default='fetch', max_length=16, verbose_name='strategy'),
        ),
        migrations.AddField(
            model_name='topology',
            name='ttl',
            field=models.PositiveIntegerField(default=0, help_text='"Time To Live" in seconds: 0 will immediately mark missing links as down; a value higher than 0 will delay marking missing links as down until the "last modified" field is older than TTL  (RECEIVE strategy)', verbose_name='TTL'),
        )
    ]
