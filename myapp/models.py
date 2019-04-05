from __future__ import unicode_literals
from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=30)
    phone=models.CharField(max_length=20)
    

    def __str__(self):
        return self.username.username

class Images(models.Model):
    chart=models.ImageField(blank=True,null=True)

class Agromain(models.Model):
    data_file = models.FileField(upload_to='data/', null=True, blank=True)
    active=models.BooleanField(default=True)

    # def __str__(self):
    #   return self.data_file
    @staticmethod
    def _set_inactive():
        data_set=Agromain.objects.all()
        if data_set:
            for data in data_set:
                data.active=False
                data.save()
    def save(self, *args, **kwargs):
        if self.pk is None:
            self._set_inactive()
        super(Agromain,self).save(*args,**kwargs)           




class Agridata(models.Model):
    state_name = models.CharField(max_length=50)
    district_name = models.CharField(max_length=50)
    crop_year = models.IntegerField(default=2002)
    season = models.CharField(max_length=50)
    crop = models.CharField(max_length=50)
    area = models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    production = models.DecimalField(default=0.0,decimal_places=2,max_digits=10)
    rainfall = models.IntegerField(default=0)
    
    def __str__(self):
        return self.state_name+'-'+self.district_name


class Contact(models.Model):
    name=models.CharField(max_length=30)
    # name=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=30)
    message=models.CharField(max_length=80)
    

    def __str__(self):
        return str(self.name)




