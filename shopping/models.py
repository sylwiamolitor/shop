from enum import Enum

from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    stock_number = models.IntegerField()
    price = models.IntegerField()
    create_time = models.DateTimeField('create time')
    last_edit_time = models.DateTimeField('last edit time')


class OrderStatus(Enum):
    NEW = "New"
    ACCEPTED = "Accepted"
    PAYMENT_RECEIVED = "Payment received"
    SHIPPED = "Shipped"


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    price = models.IntegerField()

    create_time = models.DateTimeField('create time')
    accept_time = models.DateTimeField('accept time', null=True)
    payment_time = models.DateTimeField('payment time', null=True)
    shipping_time = models.DateTimeField('shipping time', null=True)
    last_update_time = models.DateTimeField('last update time')

    @property
    def state(self):
        if self.accept_time is None:
            return OrderStatus.NEW
        elif self.payment_time is None:
            return OrderStatus.ACCEPTED
        elif self.shipping_time is None:
            return OrderStatus.PAYMENT_RECEIVED
        else:
            return OrderStatus.SHIPPED
