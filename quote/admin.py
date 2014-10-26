from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from .models import Quote




class QuoteAdmin(admin.ModelAdmin):
    model = Quote

admin.site.register(Quote, QuoteAdmin)

