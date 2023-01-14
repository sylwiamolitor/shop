from django.urls import path, include
from .views import index, addProduct, getAllProducts, getAllProductsMatchingCriteria, get, buy

urlpatterns = [
    path('', index, name="index"),
    path('add/', addProduct, name="addProduct"),
    path('get/', getAllProducts, name="getAllProducts"),
    path('get/<int:id>/', get, name='get'),
    path('buy/<int:id>/', buy, name='buy'),
    path('search/', getAllProductsMatchingCriteria, name='getAllProductsMatchingCriteria')
]