from django.test import TestCase
from django.urls import reverse, resolve
from .forms import *
from .models import *
from django.contrib.auth.models import User
from .apps import BlogConfig
from .views import *


# Create your tests here.


class TestForm(TestCase):
    def test_app(self):
        app = BlogConfig
        assert app.name == 'blog'

    def test_order_form(self):  # todo не работает
        customer = Customer.objects.create()

        artist = Artist.objects.create(name="Vincent van Gogh", description_small="small", description_big="big",
                                       quote="quote to say")
        artist.save()
        painting = Painting.objects.create(name="Starry Night", author=artist, description_small="small",
                                           description_big="big", price=123, number_available=1)
        painting.save()

        context = {'amount': 1, 'product': painting,
                   'phone_number': "12337174",
                   'shipping_address': "BSUIR"}

        form = OrderForm(data=context)

        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_sign_up_form(self):
        context = {'username': "janush", 'email': 'janush@gmail.com', 'password1': "asdaasdasdadsda",
                   'password2': "asdaasdasdadsda"}
        form = CreateUserForm(data=context)
        self.assertTrue(form.is_valid())

    def test_customer_form(self):
        user = User.objects.create_user('Janush', 'Janush@gmai.com', 'janushpassword123')
        context = {'user': user, "phone": "123", "address": "BSUIR"}
        form = CustomerForm(context)

        self.assertTrue(form.is_valid(), form.errors)


class TestModel(TestCase):

    def test_painting(self):
        artist = Artist.objects.create(name="Vincent van Gogh", description_small="small", description_big="big",
                                       quote="quote to say")
        painting = Painting.objects.create(name="Starry Night", author=artist, description_small="small",
                                           description_big="big", price=123, number_available=1)
        assert painting.author.name == "Vincent van Gogh"

    def test_mail1(self):
        mail = MyMail.objects.create(email_subject="Subject", email_text='text', email_date='2020-12-12',
                                     email_time='10:10:10', check_send=True)
        assert mail.__str__() == 'Subject'

    def test_customer(self):
        user = User.objects.create_user('Janush', 'Janush@gmai.com', 'janushpassword123')
        customer = Customer.objects.create(user=user, phone="123", address="BSUIR")
        profile = user.customer
        assert profile.verified is False

    def test_artist(self):
        artist = Artist.objects.create(name="Vincent van Gogh", description_small="small", description_big="big", )
        assert artist.quote == "No QUOTES provided"

    def test_order(self):
        order = Order.objects.create(
            amount=1,
            phone_number="12313",
            shipping_address="addres"
        )
        self.assertEqual(order.product, None)


class TestURL(TestCase):
    def test_login(self):
        path = reverse(login_page)
        self.assertEqual(resolve(path).view_name, 'login')

    def test_register(self):
        path = reverse(register_page)
        self.assertEqual(resolve(path).view_name, 'register')

    def test_logout(self):
        path = reverse(logout_user)
        self.assertEqual(resolve(path).view_name, 'logout')

    def test_profile_page(self):
        path = reverse(profile_page)
        self.assertEqual(resolve(path).view_name, 'account')


class TestView(TestCase):
    def test_login(self):
        path = reverse(login_page)
        self.assertEqual(resolve(path).view_name, 'login')
