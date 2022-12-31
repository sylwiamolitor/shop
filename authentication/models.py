from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    town_city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=12)
    country = models.CharField(max_length=100)
