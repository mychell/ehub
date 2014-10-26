# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ListingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('value', models.BooleanField(default=None)),
                ('description', models.TextField(blank=True)),
                ('attribute', models.ForeignKey(to='listings.ListingAttribute')),
                ('product', models.ForeignKey(related_name='details', to='listings.Listing')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
