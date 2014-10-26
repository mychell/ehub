# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20141023_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('attribute', models.ForeignKey(to='listings.VariationAttribute')),
                ('listing', models.ForeignKey(to='listings.Listing', related_name='vdetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='variationdetails',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='variationdetails',
            name='listing',
        ),
        migrations.DeleteModel(
            name='VariationDetails',
        ),
    ]
