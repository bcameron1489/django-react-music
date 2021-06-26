from django.conf.urls import url
from .views import main

# this is taking the url seet by music_controller/urls.py, setting any 
# endpoint designated with an empty string (homepage) and rendering the 
# 'main' method located in our views.py
urlpatterns = [
    url('', main)
]
