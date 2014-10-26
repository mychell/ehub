# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_variationdetail_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='capacity',
            field=models.IntegerField(default=50, blank=True, max_length=50),
            preserve_default=False,
        ),
    ]
