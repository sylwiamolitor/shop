from django.db import models


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stock_number = models.IntegerField()
    price = models.IntegerField()
    user = models.CharField(max_length=100)
    create_time = models.DateTimeField('create time')
    last_edit_time = models.DateTimeField('last edit time')
