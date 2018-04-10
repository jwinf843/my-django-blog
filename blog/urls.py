# Imports....I guess? lol

from django.conf.urls import url 
from . import views

# URL Patterns

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    ]
    
