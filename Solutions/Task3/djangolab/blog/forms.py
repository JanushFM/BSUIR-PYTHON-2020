from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Order, Customer


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer']
        # fields = ['product', 'amount', 'phone_number', 'shipping_address']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'verified']
