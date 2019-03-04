from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm

def login(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		user=User.objects.create(
			Phone=phone,
			password=password)
		
		return render(request,'home.html',{})
	else:
		return render(request,'login.html', {})

def register(request):
	if request.method == 'POST':
		name=request.POST.get('name')
		phone=request.POST.get('phone')
		email=request.POST.get('email')
		pass1=request.POST.get('password')
		user=User.objects.create(
			username=name,
			phoneno=phone,
			email=email,
			password=password,
			)
		userpro=user(
			username=user,
			email=email,
			phoneno=phone)

		userpro.save()
		return render(request,'login.html',{})
	else:
		return render(request,'signup.html',{})    

