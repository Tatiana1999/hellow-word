# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whois', '0006_links'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Links',
        ),
    ]
