# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0002_remove_quote_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='name',
            field=models.CharField(default=datetime.date(2014, 10, 26), max_length=100),
            preserve_default=False,
        ),
    ]
