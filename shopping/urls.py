from django.urls import path

from .views import index, addProduct, getAllProducts, get, delete, edit

urlpatterns = [
    path('', index, name="index"),
    path('add/', addProduct, name="addProduct"),
    path('get/', getAllProducts, name="getAllProducts"),
    path('get/<int:id>/', get, name='get'),
    path('delete/<int:id>/', delete, name="delete"),
    path('edit/<int:id>/', edit, name="edit"),
]
