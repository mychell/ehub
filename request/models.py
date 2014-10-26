import datetime, os, sys
from django.db import models
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.utils import timezone
from listings.models import *
from inquiry.models import *

# Create your models here.



class Request(models.Model):
	listing = models.ForeignKey(Listing, related_name = "venues")
	event = models.ForeignKey(Inquiry, related_name = "events")
	owner = models.ForeignKey(User)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % (self.listing)





    

                                 

