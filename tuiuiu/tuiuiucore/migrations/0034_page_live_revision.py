# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-26 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tuiuiucore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='tuiuiucore.PageRevision', verbose_name='live revision'),
        ),
    ]
