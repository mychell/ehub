from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from listings.views import *
from inquiry.views import *
from request.views import *
from quote.views import *
from django.conf import settings




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecenters.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#ListingListView.as_view()
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include("django.contrib.comments.urls")),
    url(r'^$', ListingListView.as_view(), name="home"),
    url(r'^login/$', "django.contrib.auth.views.login",{"template_name":"registration/login.html"}, name="login"),
    url(r'^logout/$', "django.contrib.auth.views.logout_then_login", name="logout"),
    url(r'^accounts/', include('registration.backends.simple.urls'),),
    url(r'^users/(?P<slug>\w*)/$', auth(UserProfileDetailView.as_view()), name="profile"),
    url(r'^edit_profile/$',auth(UserProfileEditView.as_view()), name="edit_profile"),
    url(r'^listing/create/$', auth(ListingCreateView.as_view()), name="listing_create"),
    url(r'^listing/edit/(?P<pk>\d+)/$', auth(ListingUpdateView.as_view()),name='listing_edit',),
    url(r'^listing/delete/(?P<pk>\d+)/$', auth(ListingDeleteView.as_view()),name='listing_delete',),
    url(r'^listing/$', ListingByUserListView.as_view(), name="listing_list"),
    
    # url(r'^variation/create/$', auth(VariationDetailCreateView.as_view()), name="variation_create"),
     url(r'^listing/detail(?P<pk>\d+)/$', ListingDetailView.as_view(), name="listing_detail"),
    url(r'^search/$',ListingSearchListView.as_view(), name="search"),
    url(r'^city/(?P<q>.+?\w*)/$',ListingSearchListView.as_view(), name="city_search"),
    url(r'^inquiry/create/$', auth(InquiryCreateView.as_view()),name='inquiry_create',),
    url(r'^inquiry/edit/(?P<pk>\d+)/$', auth(InquiryUpdateView.as_view()),name='inquiry_edit',),
    url(r'^inquiry/delete/(?P<pk>\d+)/$', auth(InquiryDeleteView.as_view()),name='inquiry_delete',),
    url(r'^inquiry/$', InquiryListView.as_view(), name="inquiry_list"),
    url(r'^request/(?P<pk>\d+)/$', RequestListView.as_view(),name='request',),
    url(r'^listing/request/(?P<pk>\d+)/$', ListingRequestView.as_view(),name='listing_request',),
    url(r'^venue/(?P<pk>\d+)/$', RequestCreateView.as_view(), name="venue_detail"),
    url(r'^quoterequest/(?P<listing_id>\d+)/$', quoterequest, name='no_of_requests'),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^booking/(?P<pk>\d+)/$', QuoteCreateView.as_view(), name="request_detail"),
    url(r'^quote/detail/(?P<pk>\d+)/$', QuoteDetailView.as_view(), name='quote_detail'),


)


urlpatterns += staticfiles_urlpatterns()


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )