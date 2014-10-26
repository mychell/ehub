# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20141023_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='variationdetail',
            name='title',
            field=models.CharField(max_length=255, default=datetime.date(2014, 10, 23)),
            preserve_default=False,
        ),
    ]
