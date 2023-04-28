from django.db import models

# Create your models here.

#we are creating  a custom user model "user acccount"
class customerRegistration(models.Model):
    firstName = models.CharField(max_length=22)
    lastName = models.CharField(max_length=10)
    date_birth =models.CharField(max_length=6)
    gender = models.CharField(max_length=6)
    country = models.CharField(max_length=6)
    state =models.CharField(max_length=6)
    zipcode =  models.IntegerField(default = 0, null=True, blank=True)
    phone_one = models.IntegerField(default = 0, null=True, blank=True)
    phone_two = models.IntegerField(default = 0, null=True, blank=True)
    email = models.CharField(max_length=30)
    town = models.CharField(max_length=6)
    password = models.CharField(max_length=22)
    signup_time = models.DateTimeField(auto_now=True)

class registration(models.Model):
    firstName = models.CharField(max_length=22 )
    gender = models.CharField(max_length=6)
    email = models.CharField(max_length=30)
    signup_time = models.DateTimeField(auto_now=True)


def __str__(self):
        return self.self.firstName
    
