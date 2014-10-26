# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20141024_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingimage',
            name='thumb',
        ),
    ]
