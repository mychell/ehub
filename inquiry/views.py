from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import *
from .models import Inquiry
from .forms import InquiryForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# Create your views here.

class InquiryCreateView(CreateView):
	model = Inquiry
	form_class = InquiryForm

	def get_success_url(self):
		return reverse("profile", kwargs={"slug": self.request.user})

	def get_context_data(self, **kwargs):
		context = super(InquiryCreateView, self).get_context_data(**kwargs)
		context['action'] = reverse('inquiry_create')
		return context

	def form_valid(self, form):
		object = form.save(commit=False)
		object.owner = self.request.user
		object.save()
		return super(InquiryCreateView, self).form_valid(form)


class InquiryUpdateView(UpdateView):
	model = Inquiry
	#slugfield = "id"
	form_class = InquiryForm

	def get_success_url(self):
		return reverse("profile", kwargs={"slug": self.request.user})

	def get_object(self, queryset=None):
		return get_object_or_404(Inquiry,pk=self.kwargs.get("pk"),owner=self.request.user,)

	def get_context_data(self, **kwargs):
		context = super(InquiryUpdateView, self).get_context_data(**kwargs)
		context['action'] = reverse('inquiry_edit',kwargs={'pk': self.get_object().id})
		return context

	# def form_valid(self, form):
	# 	object = form.save(commit=False)
	# 	object.owner = self.request.user
	# 	object.save()
	# 	return super(InquiryUpdateView, self).form_valid(form)

class InquiryDeleteView(DeleteView):
	model = Inquiry

	def get_object(self, queryset=None):
		return get_object_or_404(Inquiry,pk=self.kwargs.get("pk"),owner=self.request.user,)

	def get_success_url(self):
		return reverse("profile", kwargs={"slug": self.request.user})



class InquiryListView(ListView):
	model = Inquiry
	#queryset = Listing.with_requests.all()

	def get_queryset(self):
		queryset = Inquiry.with_requests.all()
		#self.q = self.request.GET.get('q')
		# if self.q is None:
		# 	self.q = self.kwargs['q']
		# if self.q is not None:
		queryset = queryset.filter(owner=self.request.user)
	    	
		return queryset