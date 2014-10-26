import datetime, os, sys

from django.core.files import File
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse
from PIL import Image
from django.db.models import Count

# Create your models here.

class ListingRequestCountManager(models.Manager):
    def get_queryset(self):
        return super(ListingRequestCountManager,self).get_queryset().annotate(
            requests=Count('venues')).order_by('-requests')

class ListingFeature(models.Model):
    #listing = models.ManyToManyField(Listing, related_name='features')
    #attribute = models.ForeignKey(VariationAttribute)
    title = models.CharField(max_length=255)
    #description = models.TextField(blank=True)
    #price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % (self.title)

class Listing(models.Model):

    title = models.CharField('Venue name', max_length=100)
    owner = models.ForeignKey(User)
    description = models.TextField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    #slug = models.SlugField(unique=True)
    capacity = models.IntegerField(max_length=50, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100,
                                default=00.00)
    features = models.ManyToManyField(ListingFeature, related_name="features")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    with_requests = ListingRequestCountManager()
    objects = models.Manager()

	#Venue_type = models.ForeignKey(ListingType)
    # class Meta:
    # 	unique_together = ('title', 'slug')

    def __str__(self):
    	return self.title


    def get_absolute_url(self):
        return reverse("listing_detail", kwargs={"pk": str(self.id)})

    def get_price(self):
        return self.price

	

class ListingAttribute(models.Model):

    '''
 The ListingAttribute model represents a class of feature found
 across a set of products. It does not store any data values
 related to the attribute, but only describes what kind of a
 product feature we are trying to capture. Possible attributes
 include things such as materials, colors, sizes, and many, many
 more.
 '''

    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % self.name




class ListingDetail(models.Model):

    '''
 The ListingDetail  model represents information unique to a
 specific product. This is a generic design that can be used
 to extend the information contained in the ``Product`` model with
 specific, extra details.
 '''

    listing= models.ForeignKey(Listing, related_name='details')
    attribute = models.ForeignKey(ListingAttribute)
    value = models.BooleanField(default=None)
    description = models.TextField(blank=True)

    def __str__(self):
        return '%s: %s - %s' % (self.listing, self.attribute,
                                 self.value)


class VariationAttribute(models.Model):
    name = models.CharField(max_length=300)
    #description = models.TextField(blank=True)

    def __str__(self):
        return '%s' % self.name


class VariationDetail(models.Model):
    listing = models.ForeignKey(Listing, related_name='vdetails')
    attribute = models.ForeignKey(VariationAttribute)
    title = models.CharField(max_length=255)
    #description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '%s: %s - %s' % (self.listing, self.attribute,
                                 self.price)

class ListingImage(models.Model):
    title = models.CharField(max_length=256)
    listting = models.ForeignKey(Listing, related_name='images')
    image = models.ImageField(upload_to='photos')
    #thumb = models.ImageField(upload_to='photos', editable=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return self.image.url





    # def save(self, size=(610, 460)):
    #     """
    #     Save Photo after ensuring it is not blank.  Resize as needed.
    #     """

    #     if not self.id and not self.image:
    #         return

    #     super(ListingImage, self).save()

    #     filename = self.get_source_filename()
    #     img = Image.open(filename)
    
    #     img.thumbnail(size, Image.ANTIALIAS)
    #     img.save(filename)


class UserProfile(models.Model):
	user = models.OneToOneField(User, unique=True)
	bio = models.TextField(null=True)

	def __str__(self):
		return "%s" % self.user


def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_profile, sender=User)








