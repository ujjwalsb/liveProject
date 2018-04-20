from django.conf.urls import url
from comments import views

urlpatterns = [
    url(r'^(?P<id>\d+)/delete/$', views.comment_delete, name='delete'),
    url(r'^(?P<id>\d+)/$', views.comment_thread, name='thread'),
]
