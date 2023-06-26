from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    #user status
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'phone_number']

class Client(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE, 
                                primary_key=True, 
                                related_name='client')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
                                    max_length=17, 
                                    blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Seller(models.Model):
    user = models.OneToOneField(User, 
                            on_delete=models.CASCADE, 
                            primary_key=True, 
                            related_name='seller')
    belongs_to = models.ForeignKey('shop.organization', 
                                    on_delete=models.CASCADE, 
                                    related_name='organization_reff')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
                                    max_length=17, 
                                    blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






"""
belongs_to = models.ForeignKey("organizations.Organization", on_delete=models.CASCADE, related_name='')
"""