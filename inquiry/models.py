import datetime, os, sys
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils import timezone
from django.db.models import Count

# Create your models here.


class InquiryRequestCountManager(models.Manager):
    def get_queryset(self):
        return super(InquiryRequestCountManager,self).get_queryset().annotate(
            requests=Count('events')).order_by('-requests')



class Inquiry(models.Model):
	name = models.CharField(max_length=255, blank=False)
	owner = models.ForeignKey(User)
	email = models.EmailField(blank=False)
	phone = models.CharField(max_length=30)
	organization = models.CharField(max_length=255)
	event_date = models.DateField(verbose_name="Proposed Event Date", blank=False)
	total_budget = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	additional_info = models.TextField(blank = True)
	site_visit = models.BooleanField(default=False, verbose_name="I would like to schedule a site visit")
	other_venues = models.BooleanField(default=False, verbose_name="I would like to consider other venues")
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	with_requests = InquiryRequestCountManager()
	objects = models.Manager()

	def __str__(self):
		return '%s - %s ' % (self.name, self.event_date)




    

                                 

