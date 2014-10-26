from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import *


class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 0

class ListingDetailInline(admin.TabularInline):
    model = ListingDetail
    extra = 0

class VaritionDetailInline(admin.TabularInline):
    model = VariationDetail
    extra = 0


class ListingAdmin(admin.ModelAdmin):
	inlines = [ ListingImageInline, ]

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

class UserProfileAdmin(UserAdmin):
	inlines=(UserProfileInline,)

class ListingAttributeAdmin(admin.ModelAdmin):
    model = ListingAttribute
class VariationAttributeAdmin(admin.ModelAdmin):
    model = VariationAttribute

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
admin.site.register(Listing, ListingAdmin)
# admin.site.register(ListingAttribute, ListingAttributeAdmin)
# admin.site.register(VariationAttribute, VariationAttributeAdmin)
admin.site.register(ListingFeature)