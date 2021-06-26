from django.conf.urls import url
from .views import RoomView

# this is taking the url seet by music_controller/urls.py, setting any 
# endpoint designated with an empty string (homepage) and rendering the 
# 'main' method located in our views.py
urlpatterns = [
    url('home', RoomView.as_view()),
]
