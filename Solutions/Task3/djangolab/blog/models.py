from multiprocessing.pool import ThreadPool
from django.core.mail import EmailMessage
from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from multiprocessing import Pool
# Create your models here.
from django.template.loader import render_to_string

from mysite import settings


class Artist(models.Model):
    name = models.CharField(max_length=122, null=True)
    description_small = models.TextField(max_length=200, null="No SMALL description provided")
    description_big = models.TextField(max_length=4000, null="No BIG description provided")
    photo = models.ImageField(null=True, blank=True)
    quote = models.TextField(max_length=400, default="No QUOTES provided")

    def __str__(self):
        return self.name


class Painting(models.Model):
    name = models.CharField(max_length=122, null=True)
    author = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    description_small = models.CharField(max_length=122, null=True, default="No SMALL description provided")
    description_big = models.CharField(max_length=4000, null=True, default="No BIG description provided")
    price = models.DecimalField(null=True, max_digits=19, decimal_places=0)
    number_available = models.IntegerField(null=True)
    image_file = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Painting, null=True, on_delete=models.CASCADE)  # one to many relationship
    amount = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=40, null=True)
    shipping_address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.product.name


class MyMail(models.Model):
    email_subject = models.CharField('Заголовок сообщения', max_length=100)
    email_text = models.TextField('Текст сообщения', null=True)
    email_date = models.DateField('Время отправки', null=True)
    email_time = models.TimeField(null=True)
    recipients = models.ManyToManyField(Customer)
    check_send = models.BooleanField(default=False)

    def __str__(self):
        if self.check_send is False:
            self.check_send = True
            self.send_message()
            self.save()
        return str(self.email_subject)

    def send_message(self):
        context = {'text': self.email_text, 'date': self.email_date, 'time': self.email_time}

        message = render_to_string('blog/email_to_users.html', context)

        list_messages = []
        for recipient in self.recipients.all():
            list_messages.append(
                EmailMessage(self.email_subject, message, settings.EMAIL_HOST_USER, [recipient.user.email]))

        pool = ThreadPool(processes=len(list_messages))
        pool.map(send_m_pool, list_messages)  # list messages - argument in send_m_pool


def send_m_pool(message):
    message.send()
