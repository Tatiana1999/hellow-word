# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('whois', '0007_delete_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='Linksp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('fecha', models.TextField()),
            ],
        ),
    ]