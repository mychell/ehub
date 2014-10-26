# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_listing_capacity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='created_date',
        ),
        migrations.AddField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 24), auto_now_add=True),
            preserve_default=False,
        ),
    ]
