
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculate, name='calculate'),
    path('allcurrencies/', views.allcurrencies, name='currencies'),
    path('addcurrencies/', views.add_curr, name='add_currencies')
]
