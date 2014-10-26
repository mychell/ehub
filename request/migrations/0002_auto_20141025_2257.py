# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='event',
            field=models.ForeignKey(related_name='events', to='inquiry.Inquiry'),
        ),
        migrations.AlterField(
            model_name='request',
            name='listing',
            field=models.ForeignKey(related_name='venues', to='listings.Listing'),
        ),
    ]
