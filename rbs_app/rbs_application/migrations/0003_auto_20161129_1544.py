# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbs_application', '0002_category_category_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Complaints',
            new_name='Complaint',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
    ]
