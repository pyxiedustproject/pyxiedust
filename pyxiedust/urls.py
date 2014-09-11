from django.conf.urls import patterns, include, url
from django.contrib import admin

from pyxiedust import views as main_views
from blog import views as blog_views
from tasks import views as tasks_views
from food import views as food_views

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

    # Admin pages
    url(r'^admin/', include(admin.site.urls)),
)
