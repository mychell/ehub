from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404,  render_to_response
from django.views.generic import *
from django.core.urlresolvers import reverse
from .forms import UserProfileForm, ListingForm, SearchForm, VariationDetailForm, VariationDetailFormSet 
from .models import Listing, UserProfile, VariationDetail
from inquiry.models import Inquiry
from request.models import Request

# Create your views here.

class ListingListView(ListView):
	model = Listing
	paginate_by = 3 
	
	template_name = 'listing_list.html'

	def get_context_data(self,**kwargs):
		context = super(ListingListView, self).get_context_data(**kwargs)
		context['cities'] = Listing.objects.values('city').distinct()
		return context

class ListingByUserListView(ListView):
	model = Listing
	#queryset = Listing.with_requests.all()

	def get_queryset(self):
		queryset = Listing.with_requests.all()
		#self.q = self.request.GET.get('q')
		# if self.q is None:
		# 	self.q = self.kwargs['q']
		# if self.q is not None:
		queryset = queryset.filter(owner=self.request.user)
	    	
		return queryset


class ListingDetailView(DetailView):
	model = Listing

class ListingSearchListView(ListView):
	#model = Listing
	template_name = 'listings/listing_search.html'

	# def get(self, request, *args, **kwargs):
	# 	form = SearchForm(self.request.GET or None)
	# 	if form.is_valid():
	# 		self.listings = Listing.objects.filter(city__icontains=form.cleaned_data['query'])
	# 	return self.render_to_response(self.get_context_data(form=form))

	def get_object(self):
		self.q = self.kwargs["q"]
        

	def get_queryset(self):
		queryset = Listing.objects.all()
		self.q = self.request.GET.get('q')
		if self.q is None:
			self.q = self.kwargs['q']

		if self.q is not None:
		    queryset = queryset.filter(city__icontains=self.q)

		else:
			queryset = queryset.objects.all()
	    	
		return queryset

	def get_context_data(self, **kwargs):
		context = super(ListingSearchListView, self).get_context_data(**kwargs)
		context['q'] = self.q
		return context
		
 
class ListingCreateView(CreateView):
	model = Listing
	form_class = ListingForm

    

	def form_valid(self, form):
		f = form.save(commit=False)
		f.owner = self.request.user
		f.save()
		return super(ListingCreateView,self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(ListingCreateView, self).get_context_data(**kwargs)
		context['action'] = reverse('listing_create')
		return context

	def get_success_url(self):
		return reverse("profile", kwargs={"slug": self.request.user})

class ListingUpdateView(UpdateView):
	model = Listing
	form_class = ListingForm

	def get_context_data(self, **kwargs):
		context = super(ListingUpdateView, self).get_context_data(**kwargs)
		context['action'] = reverse('listing_edit',kwargs={'pk': self.get_object().id})
		return context

	def get_object(self, queryset=None):
		return get_object_or_404(Listing,pk=self.kwargs.get("pk"),owner=self.request.user,)

	def get_success_url(self):
		return reverse("profile", kwargs={"slug": self.request.user})


class ListingDeleteView(DeleteView):
	model = Listing

	def get_object(self, queryset=None):
		return get_object_or_404(Listing,pk=self.kwargs.get("pk"),owner=self.request.user,)

	def get_success_url(self):
		return reverse("profile", kwargs={"slug": self.request.user})

# class VariationDetailCreateView(CreateView):
# 	model = VariationDetail
# 	form_class = VariationDetailFormSet 

# 	def get_context_data(self,**kwargs):
# 		context = super(ListingListView, self).get_context_data(**kwargs)
# 		variation_formset = VariationDetailFormSet (instance=VariationDetail
# 		context['cities'] = Listing.objects.values('city').distinct()
# 		return context

    

# 	def form_valid(self, form):
# 		f = form.save(commit=False)
# 		f.owner = self.request.user
# 		f.save()
# 		return super(ListingCreateView,self).form_valid(form)

# 	def get_success_url(self):
# 		return reverse("profile", kwargs={"slug": self.request.user})


class UserProfileDetailView(DetailView):
	model = get_user_model()
	slug_field = "username"

	template_name ="user_detail.html"

	def get_object(self, queryset=None):
		user = super(UserProfileDetailView, self).get_object(queryset)
		UserProfile.objects.get_or_create(user=user)
		return user

	def get_context_data(self, **kwargs):
		context = super(UserProfileDetailView, self).get_context_data(**kwargs)
		context['inquiries'] = Inquiry.objects.filter(owner = self.request.user)
		context['listings'] = Listing.objects.filter(owner = self.request.user)
		return context

class UserProfileEditView(UpdateView):
	model = UserProfile
	form_class = UserProfileForm
	template_name ="edit_profile.html"

	def get_object(self, queryset=None):
		return UserProfile.objects.get_or_create(user=self.request.user)[0]

	def get_success_url(self):
		return reverse("profile", kwargs={"slug": self.request.user})


def quoterequest(request, listing_id):
    try:
        r = Request.objects.filter(listing__pk = listing_id).count()
    except Listing.DoesNotExist:
        raise Http404
    return render_to_response('listings/no_of_quotes.html', {'request_no': r})