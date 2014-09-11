from django.conf.urls import patterns, include, url
from django.contrib import admin

from pyxiedust import views as main_views

urlpatterns = patterns('',
    url(r'^$', main_views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
