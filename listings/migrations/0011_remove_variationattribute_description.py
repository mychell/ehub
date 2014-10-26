# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_remove_variationdetail_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variationattribute',
            name='description',
        ),
    ]
