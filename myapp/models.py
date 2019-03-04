from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

class UserProfile(models.Model):
	username=models.ForeignKey(User,on_delete=models.CASCADE)
	email=models.CharField(max_length=30)
	phone_no=models.CharField(max_length=20)
	

	def _str_(self):
		return self.user.username
class Agromain(models.Model):
	data_file=models.CharField(max_length=100)
	active=models.IntegerField()

	def _str_(self):
		return self.active

class Agridata(models.Model):
	state_name=models.CharField(max_length=50)
	district_name=models.CharField(max_length=50)	
	crop_year=models.IntegerField()
	season=models.CharField(max_length=50)
	crop=models.CharField(max_length=50)
	area=models.DecimalField(max_digits=10,decimal_places=4,default=Decimal('0.0000'))
	production=models.DecimalField(max_digits=10,decimal_places=4,default=Decimal('0.0000'))
	rainfall=models.IntegerField()
	
	def _str_(self):
		return self.state_name,self.production