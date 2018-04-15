# Imports....I guess? lol

from django.conf.urls import url 
from . import views

#    The Preview Commands: 
#        python manage.py runserver 0.0.0.0:8080

# URL Patterns

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    ]
    
