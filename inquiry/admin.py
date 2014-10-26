from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import Inquiry




class InquiryAdmin(admin.ModelAdmin):
    model = Inquiry

admin.site.register(Inquiry, InquiryAdmin)

