from django.shortcuts import render
from django.views.generic import CreateView
from .form import clientSignUpForm, sellerSignUpForm
from .models import User, Client, Seller

def register(request):
    return render(request, '../templates/register.html')

class client_register(CreateView):
    model = User
    form_class = clientSignUpForm 
    template_name = '../templates/cutomer_ergister.html'


class seller_register(CreateView):
    model = User
    form_class = sellerSignUpForm
    template_name = '../templates/seller_ergister.html'