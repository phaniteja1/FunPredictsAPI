# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-02 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('image_url', models.URLField(blank=True, max_length=128)),
            ],
            options={
                'verbose_name': 'Prediction',
                'verbose_name_plural': 'Predictions',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('price_change_value', models.CharField(max_length=255)),
                ('price_change', models.CharField(choices=[('P', 'positive'), ('N', 'negative')], max_length=1)),
                ('prediction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='predictions.Prediction')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
    ]