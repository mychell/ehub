from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import *
from django.core.urlresolvers import reverse
from inquiry.models import Inquiry
from listings.models import Listing

from .models import *
from .forms import *


class RequestListView(ListView):
	model = Request
	#template_name = 'listings/listing_search.html'

	# def get(self, request, *args, **kwargs):
	# 	form = SearchForm(self.request.GET or None)
	# 	if form.is_valid():
	# 		self.listings = Listing.objects.filter(city__icontains=form.cleaned_data['query'])
	# 	return self.render_to_response(self.get_context_data(form=form))

	# def get_object(self):
	# 	self.q = self.kwargs["q"]
        

	def get_queryset(self):
		queryset = Request.objects.all()
		self.q = self.request.GET.get('pk')
		if self.q is None:
			self.q = self.kwargs['pk']
		if self.q is not None:
		    queryset = queryset.filter(event__pk=self.q)
	    	
		return queryset

	def get_context_data(self, **kwargs):
		context = super(RequestListView, self).get_context_data(**kwargs)
		#context['inquiries'] = Inquiry.objects.filter(owner = self.request.user)
		#context['listing'] = Listing.objects.filter(pk = self.q)
		context['inquiry'] = get_object_or_404(Inquiry,pk=self.q)
		return context


# class RequestCreateView(CreateView):
# 	model = Request
# 	form_class = RequestForm

# 	def get_success_url(self):
# 		return reverse("profile", kwargs={"slug": self.request.user})

# 	# def get_context_data(self, **kwargs):
# 	# 	context = super(InquiryCreateView, self).get_context_data(**kwargs)
# 	# 	context['action'] = reverse('inquiry_create')
# 	# 	return context

# 	def form_valid(self, form):
# 		object = form.save(commit=False)
# 		object.owner = self.request.user
# 		object.save()
# 		return super(InquiryCreateView, self).form_valid(form)



class RequestCreateView(CreateView):
    """Creates a Product for a Shop."""
    model = Request
    form_class = RequestForm

    def get_form_kwargs(self):
        kwargs = super(RequestCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """Associate the Shop with the new Product before saving."""
        form.instance.listing = self.listing
        form.instance.owner = self.request.user
        return super(RequestCreateView, self).form_valid(form)

    def dispatch(self, *args, **kwargs):
        """Ensure the Shop exists before creating a new Product."""
        self.listing = get_object_or_404(Listing, pk=kwargs['pk'])
        return super(RequestCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Add current shop to the context, so we can show it on the page."""
        context = super(RequestCreateView, self).get_context_data(**kwargs)
        context['listing'] = self.listing
        context['request'] = Inquiry.objects.filter(owner=self.request.user)
        return context

    def get_success_url(self):
    	return reverse("profile", kwargs={"slug": self.request.user})


class ListingRequestView(TemplateView):
    template_name = "request/displaylistingrequest.html"

    # def get_queryset(self):
    # 	queryset = Request.objects.all()
    # 	# self.q = self.request.GET.get('pk')
    # 	# if self.q is None:
    # 	self.q = self.kwargs['pk']
    # 	if self.q is not None:
    # 		queryset = queryset.filter(listing__pk=self.q)
    # 	return queryset

    def get_context_data(self, **kwargs):
        context = super(ListingRequestView, self).get_context_data(**kwargs)
        context['requests'] = Request.objects.filter(listing__pk=self.kwargs['pk'])
        return context