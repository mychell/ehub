from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import Request




class RequestAdmin(admin.ModelAdmin):
    model = Request

admin.site.register(Request, RequestAdmin)