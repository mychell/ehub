# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0005_remove_inquiry_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='created',
            field=models.DateTimeField(default=datetime.date(2014, 10, 24), auto_now_add=True),
            preserve_default=False,
        ),
    ]
