from django import forms
from django.forms.models import inlineformset_factory
from .models import *
from django.forms.widgets import CheckboxSelectMultiple



class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ("user",)



class ListingForm(forms.ModelForm):
	class Meta:
		model = Listing
		exclude = ("owner",)

	def __init__(self, *args, **kwargs):
		super(ListingForm, self).__init__(*args, **kwargs)
		self.fields["features"].widget = CheckboxSelectMultiple()
		self.fields["features"].queryset = ListingFeature.objects.all() 

#ListingImageFormSet = inlineformset_factory(Listing,ListingImage)


class VariationDetailForm(forms.ModelForm):
	class Meta:
		model = VariationDetail
		
#VariationDetailFormSet = inlineformset_factory(VariationDetail,VariationDetailForm)
BaseInlineFormSet = inlineformset_factory(Listing, VariationDetail)
VariationDetailFormSet = inlineformset_factory(VariationAttribute, VariationDetail,formset=BaseInlineFormSet, form=VariationDetailForm, extra=1)





class SearchForm(forms.ModelForm):
	query = forms.CharField()