from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from pyxiedust import views as main_views
from blog import views as blog_views
from tasks import views as tasks_views
from food import views as food_views
from photos import views as photo_views


# Here we define all the pages that are available on the site.
# We use this strange syntax called "regular expressions" which is why
# we have the characters like ^ or $.

urlpatterns = patterns('',
    url(r'^$', main_views.home, name='home'),

    # Blog pages
    url(r'^blog/$', blog_views.post_list, name='post_list'),
    url(r'^blog/(?P<post_id>\d+)/$', blog_views.post_detail, name='post_detail'),

    # Todo pages
    url(r'^tasks/$', tasks_views.task_list_todo, name='task_list_todo'),
    url(r'^tasks/all/$', tasks_views.task_list_all, name='task_list_all'),

    # Food pages
    url(r'^food/top5/$', food_views.top5, name='food_top5'),

    # Photo pages
    url(r'^gallery/$', photo_views.gallery, name='gallery'),

    # Admin pages
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login, name='login'),
)

if settings.DEBUG:
    # This bit of code makes sure the images are displayed on the gallery
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
