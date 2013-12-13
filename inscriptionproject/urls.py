from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from inscrire.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^inscrire/', include('inscrire.urls', namespace="inscrire")),
     url(r'^', include(admin.site.urls)),
    
    #url(r'^$', 'inscriptionproject.views.home', name='home'),
    # url(r'^inscriptionproject/', include('inscriptionproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
