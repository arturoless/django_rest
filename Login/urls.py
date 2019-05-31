from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Login.views import CustonAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^',include(router.urls)),
    re_path(r'^api/v1/login', include('Login.urls')),
    re_path(r'^api/v1/example', include('Example.urls'))
]