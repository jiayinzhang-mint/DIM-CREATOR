# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-09-11 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ware3D',
            fields=[
                ('workid', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('opendate', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'warehouse',
                'managed': False,
            },
        ),
    ]
