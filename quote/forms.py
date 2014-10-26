from django import forms
from django.forms.models import inlineformset_factory
from .models import Quote
from request.models import *



class QuoteForm(forms.ModelForm):
	class Meta:
		model = Quote
		exclude = ("owner","quoterequest")
		#event = forms.ModelChoiceField(queryset=Inquiry.objects.filter(owner=kwargs.pop('user')))

	# def __init__(self, *args, **kwargs):
	# 	user = kwargs.pop('user')
	# 	super(QuoteForm, self).__init__(*args, **kwargs)
	# 	qs = .objects.filter(owner=user)
	# 	#self.fields['events'] = forms.ModelChoiceField(queryset=qs)
	# 	self.fields['event'].queryset = Inquiry.objects.filter(owner=user)


