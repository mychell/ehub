# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0003_inquiry_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inquiry',
            old_name='author',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
