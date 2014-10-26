# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0004_auto_20141024_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiry',
            name='created_date',
        ),
    ]
