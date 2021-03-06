# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('filename', models.CharField(max_length=128)),
                ('hash_value', models.CharField(max_length=128)),
                ('original_filename', models.CharField(max_length=128)),
                ('size', models.IntegerField(default=0)),
                ('created', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
                ('token', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=64)),
            ],
        ),
    ]
