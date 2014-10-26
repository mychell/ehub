# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_remove_variationattribute_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListingFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='listing',
            name='feature',
            field=models.ManyToManyField(related_name='features', to='listings.ListingFeature'),
            preserve_default=True,
        ),
    ]
