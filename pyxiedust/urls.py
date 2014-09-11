from django.conf.urls import patterns, include, url
from django.contrib import admin

from pyxiedust import views as main_views
from blog import views as blog_views

urlpatterns = patterns('',
    url(r'^$', main_views.home, name='home'),

    url(r'^blog/$', blog_views.post_list, name='post_list'),
    url(r'^blog/(?P<post_id>\d+)/$', blog_views.post_detail, name='post_detail'),

    url(r'^admin/', include(admin.site.urls)),
)
