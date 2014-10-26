from django import forms
from django.forms.models import inlineformset_factory
from .models import Inquiry



class InquiryForm(forms.ModelForm):
	class Meta:
		model = Inquiry
		exclude = ("owner",)