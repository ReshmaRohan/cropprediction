from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import patterns, url
from . import views


urlpatterns = [
 
   url(r'^signup/', views.signup, name='signup_url'),
   url(r'^login/', views.log_in, name='login_url'),
   url(r'^home/',views.home,name='home_url'),
   url(r'^logout/',views.log_out,name='logout_url'),
  
   ]

urlpatterns +=  url(r'^$',views.home),
