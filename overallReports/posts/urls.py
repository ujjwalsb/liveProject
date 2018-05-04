# -*- coding: utf-8 -*-

from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.post_create, name='create'),
    url(r'^about-us/$', views.about_us),
    url(r'^services/$', views.services),
    url(r'^terms-of-use/$', views.terms_of_use),
    url(r'^ask/$', views.ask),
    url(r'^suggestion/$', views.suggestion),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
]
