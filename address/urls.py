from django.conf.urls import include, url
from django.contrib import admin
from addapp.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'address.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^address/',address),
    url(r'^show/',show),
    # url(r'^show/', show_map),
]
