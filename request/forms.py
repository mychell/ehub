from django import forms
from django.forms.models import inlineformset_factory
from .models import Request
from inquiry.models import *



class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		exclude = ("listing","owner",)
		#event = forms.ModelChoiceField(queryset=Inquiry.objects.filter(owner=kwargs.pop('user')))

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user')
		super(RequestForm, self).__init__(*args, **kwargs)
		qs = Inquiry.objects.filter(owner=user)
		#self.fields['events'] = forms.ModelChoiceField(queryset=qs)
		self.fields['event'].queryset = Inquiry.objects.filter(owner=user)


