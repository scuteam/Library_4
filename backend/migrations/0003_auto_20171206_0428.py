# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 04:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20171206_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateField(db_column=b'borrow_date', default=datetime.datetime(2017, 12, 6, 4, 28, 22, 541079)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(db_column=b'return_date', default=datetime.datetime(2017, 12, 21, 4, 28, 22, 541103)),
        ),
        migrations.AlterUniqueTogether(
            name='borrow',
            unique_together=set([]),
        ),
    ]
