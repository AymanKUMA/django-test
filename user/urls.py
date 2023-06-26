from django.urls import path
from .import  views

urlpatterns=[
    path('register/',views.register, name='register'),
    path('costumer_register/',views.costumer_register.as_view(), name='costumer_register'),
    path('seller_register/',views.seller_register.as_view(), name='seller_register'),
]