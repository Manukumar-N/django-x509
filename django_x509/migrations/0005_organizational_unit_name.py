# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-16 14:18
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('django_x509', '0004_auto_20171207_1450')]

    operations = [
        migrations.AddField(
            model_name='ca',
            name='organizational_unit_name',
            field=models.CharField(
                blank=True, max_length=64, verbose_name='organizational unit name'
            ),
        ),
        migrations.AddField(
            model_name='cert',
            name='organizational_unit_name',
            field=models.CharField(
                blank=True, max_length=64, verbose_name='organizational unit name'
            ),
        ),
    ]
