# Generated by Django 2.2 on 2019-04-23 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='takedown_time',
            field=models.TimeField(default=datetime.time(16, 17, 59, 677272)),
        ),
    ]
