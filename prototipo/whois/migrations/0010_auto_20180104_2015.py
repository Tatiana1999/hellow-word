# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whois', '0009_remove_linksp_fecha'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Linksp',
            new_name='Enlaces',
        ),
    ]