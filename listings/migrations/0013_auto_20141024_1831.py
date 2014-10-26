# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0012_auto_20141024_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='feature',
            new_name='features',
        ),
    ]
