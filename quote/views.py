
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import *
from django.core.urlresolvers import reverse
from inquiry.models import Inquiry
from listings.models import Listing
from request.models import Request

from .models import *
from .forms import *



class QuoteCreateView(CreateView):
    
    model = Quote
    form_class = QuoteForm

    # def get_form_kwargs(self):
    #     kwargs = super(QuoteCreateView, self).get_form_kwargs()
    #     kwargs.update({'user': self.request.user})
    #     return kwargs

    # def form_valid(self, form):
    #     """Associate the Shop with the new Product before saving."""
    #     form.instance.request = self.request
    #     form.instance.owner = self.request.user
    #     return super(QuoteCreateView, self).form_valid(form)

    def form_valid(self, form):
    	f = form.save(commit=False)
    	f.owner = self.request.user
    	f.quoterequest = self.req
    	f.save()
    	return super(QuoteCreateView,self).form_valid(form)

    def dispatch(self, *args, **kwargs):
        """Ensure the Shop exists before creating a new Product."""
        self.req = get_object_or_404(Request, pk=kwargs['pk'])
        return super(QuoteCreateView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """Add current shop to the context, so we can show it on the page."""
        context = super(QuoteCreateView, self).get_context_data(**kwargs)
        #context['listing'] = self.listing
        context['request'] = self.req
        return context

    def get_success_url(self):
    	return reverse("profile", kwargs={"slug": self.request.user})



class QuoteDetailView(TemplateView):
    template_name = "quote/displayquotes.html"

    # def get_queryset(self):
    # 	queryset = Request.objects.all()
    # 	# self.q = self.request.GET.get('pk')
    # 	# if self.q is None:
    # 	self.q = self.kwargs['pk']
    # 	if self.q is not None:
    # 		queryset = queryset.filter(listing__pk=self.q)
    # 	return queryset

    def get_context_data(self, **kwargs):
        context = super(QuoteDetailView, self).get_context_data(**kwargs)
        context['quotes'] = Quote.objects.filter(quoterequest__pk=self.kwargs['pk'])
        return context
