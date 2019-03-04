from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns, url
from . import views


urlpatterns = [
   url(r'^register/',views.register,name='signup_url'),
   url(r'^login/',views.login,name='login_url'),
   ]