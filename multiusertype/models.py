from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_Patient = models.CharField(max_length=7)
    is_Doctor = models.CharField(max_length=6)
    first_name = models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    profileimg=models.ImageField(upload_to='profile_images',default='Success.png')
    Area=models.CharField(max_length=400,default='area')
    city=models.CharField(max_length=400,default='city')
    state=models.CharField(max_length=400,default='state')
    pincode=models.IntegerField(default=0)
