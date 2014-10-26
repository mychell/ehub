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
from request.models import *

from quote.extra import ContentTypeRestrictedFileField

# Create your models here.





class Quote(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(
        upload_to='quotes',
        
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #event = models.ForeignKey(Inquiry, related_name = "events")
    quoterequest = models.ForeignKey(Request, related_name = "requests")
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name




    

                                 

