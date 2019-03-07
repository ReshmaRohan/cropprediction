from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.urlresolvers import reverse

def log_in(request):
	if request.method == 'POST':
		phone=request.POST.get('phone')
		password=request.POST.get('password')
		user=authenticate(username=phone,password=password)
		print user,phone,password
		if user :
			userpro=UserProfile.objects.get(username=user)
			
			if userpro :
				login(request,user)
				return HttpResponseRedirect(reverse('home_url'))
			else:
				return render(request,'login.html',{'error':"sorry,unable to login"})

		else:
			return render(request,'login.html',{'error':"sorry,unable to login"})
	else:
		return render(request,'login.html',{})      


def signup(request):
	if request.method == 'POST':
		name=request.POST.get('name')
		phone=request.POST.get('phone')
		email=request.POST.get('email')
		password_=request.POST.get('pass1')
		user=User.objects.create_user(
			username=phone,
			email=email,
			password=password_,
			)
			
		userpro=UserProfile(
			username=user,
			email=email,
			phone=phone)

		userpro.save()
		return render(request,'login.html',{})
	else:
		return render(request,'signup.html',{})    

def home(request):
	return render(request,'home.html',{})
def log_out(request):
	logout(request)
	return render(request,'home.html',{})	