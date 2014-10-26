# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listingattribute_listingdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationAttribute',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VariationDetails',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, null=True, max_digits=100, blank=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('attribute', models.ForeignKey(to='listings.VariationAttribute')),
                ('listing', models.ForeignKey(to='listings.Listing', related_name='vdetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='published_date',
            new_name='updated',
        ),
        migrations.RenameField(
            model_name='listingdetail',
            old_name='product',
            new_name='listing',
        ),
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='listingimage',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
