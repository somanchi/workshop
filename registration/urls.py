from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
from registration.views import Home
from registration.views import UserRegistrationView
from registration.views import AddChocolateview



import registration.views as views
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'prasad.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
    url(r'^user/$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='success.html'),name='user_registration_success'),
    url(r'^registration/', UserRegistrationView.as_view(), name='register_user'),
    url(r'^chocolate/add/$', AddChocolateview.as_view(), name='add_chocolate'),
)
