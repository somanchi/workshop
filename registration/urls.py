from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from registration import views
from registration.views import *
from registration.models import *
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, include,url
from django.contrib import admin
from registration.views import Home
from registration.views import UserRegistrationView
from prasad.views import anonymous_required
import registration.views as views
from registration.views import *


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'prasad.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
    url(r'^user/$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='success.html'),name='user_registration_success'),
    url(r'^registration/', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/profile/view/$', UserProfileView.as_view(), name='profile_view'),
    url(r'^chocolate/add/$', AddChocolateview.as_view(), name='add_chocolate'),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info"),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='user_profile_update'),
)
