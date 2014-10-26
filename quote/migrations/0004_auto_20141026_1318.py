# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_quote_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='request',
            new_name='quoterequest',
        ),
    ]
