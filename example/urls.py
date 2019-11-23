from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from example import views

urlpatterns = [
    re_path(r'example_lista/$', views.ExampleList.as_view()),
    re_path(r'imagen_lista/$', views.ImagenList.as_view()),
    re_path(r'person/$', views.PersonList.as_view()),
    re_path(r'person/(?P<id>\d+)$', views.PersonView.as_view()),
]