from django.urls import path, include
from .views import index, addOrder, getAllOrders, get, delete, edit

urlpatterns = [
    path('', index, name="index"),
    path('add/', addOrder, name="addOrder"),
    path('get/', getAllOrders, name="getAllOrders"),
    path('get/<int:id>/', get, name='get'),
    path('delete/<int:id>/', delete, name="delete"),
    path('edit/<int:id>/', edit, name="edit"),
]