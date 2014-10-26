# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('phone', models.CharField(max_length=30)),
                ('organization', models.CharField(max_length=255)),
                ('event_date', models.DateField(verbose_name='Proposed Event Date')),
                ('total_budget', models.DecimalField(null=True, max_digits=100, decimal_places=2, blank=True)),
                ('additional_info', models.TextField(blank=True)),
                ('site_visit', models.BooleanField(verbose_name='I would like to schedule a site visit', default=False)),
                ('other_venues', models.BooleanField(verbose_name='I would like to consider other venues', default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
