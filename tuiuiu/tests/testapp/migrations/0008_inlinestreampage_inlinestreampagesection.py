# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import tuiuiu.tuiuiucore.blocks
import tuiuiu.tuiuiucore.fields
import tuiuiu.tuiuiuimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('tuiuiucore', '0029_unicode_slugfield_dj19'),
        ('tests', '0007_jadeformpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='InlineStreamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tuiuiucore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('tuiuiucore.page',),
        ),
        migrations.CreateModel(
            name='InlineStreamPageSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('body', tuiuiu.tuiuiucore.fields.StreamField((('text', tuiuiu.tuiuiucore.blocks.CharBlock()), ('rich_text', tuiuiu.tuiuiucore.blocks.RichTextBlock()), ('image', tuiuiu.tuiuiuimages.blocks.ImageChooserBlock())))),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='tests.InlineStreamPage')),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
