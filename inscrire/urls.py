from django.conf.urls import patterns, include, url
from inscrire import views

urlpatterns = patterns('',
    url(r'^faculte/$', views.view_faculte, name='facultes'),

)
