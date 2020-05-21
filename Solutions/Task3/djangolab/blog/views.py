from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from blog.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# my forms
from .tokens import account_activation_token
from .forms import OrderForm, CreateUserForm, CustomerForm
from .decorators import unauthenticated_user


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            Customer.objects.create(  # others fields stay default (null=True) they are "none"
                user=user,

            )
            subject = 'Activate your account'
            template = render_to_string('blog/email.html', {
                'name': user.username,
                'email': user.email,
                'domain': "janush-fm.herokuapp.com",
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            user.email_user(subject, template)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'blog/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_staff:  # if user has admin attribute
                return redirect('home')
            else:
                return redirect('account')

        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'blog/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def album(request, artist_name):
    author = Artist.objects.get(name=artist_name)
    paintings = author.painting_set.all()
    is_staff = request.user.is_staff
    context = {'paintings': paintings, 'is_staff': is_staff}
    return render(request, 'blog/album_paintings.html', context)


def album_of_artists(request):
    artists = Artist.objects.all()
    context = {'artists': artists}
    return render(request, 'blog/album_artists.html', context)


def biography(request, artist_name):
    artist = Artist.objects.get(name=artist_name)
    return render(request, 'blog/biography.html', {'artist': artist})


@login_required(login_url='login')  # if user isn't logged in
def shopping_list(request):
    total_price = 0
    if request.user.is_staff:  # if user has admin attribute
        return redirect('login')
    else:
        orders = request.user.customer.order_set.all()
        for order in orders:
            total_price += order.amount * order.product.price
        context = {'orders': orders, "total_price": total_price}
        return render(request, 'blog/shopping_list.html', context)


@login_required(login_url='login')  # if user isn't logged in
def create_order(request, order_id):
    customer = request.user.customer
    customer_orders = customer.order_set.all()
    painting = Painting.objects.get(id=order_id)
    order = customer_orders.filter(product=painting)
    painting.number_available -= 1
    painting.save()
    if not order.count():  # if there is no such order
        Order.objects.create(
            customer=request.user.customer,
            product=Painting.objects.get(id=order_id),
            amount=1,
            phone_number=customer.phone,
            shipping_address=customer.address,
        )
    else:
        order = customer_orders.get(product=painting)
        order.amount += 1

        order.product.save()
        order.save()
    return redirect('/')


def update_order(request, order_id):
    order = Order.objects.get(id=order_id)
    prev_amount = order.amount
    form = OrderForm(instance=order)
    max_number = order.product.number_available + order.amount
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            constr = prev_amount - form.cleaned_data.get("amount")
            order.product.number_available += constr
            order.product.save()
            form.save()
            return redirect('shopping_list')

    context = {'form': form, 'max': max_number}
    return render(request, 'blog/order_form.html', context)


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
        order.product.number_available += order.amount
        order.product.save()
        order.delete()
        return redirect('shopping_list')

    context = {'item': order}
    return render(request, 'blog/delete_order.html', context)


@login_required(login_url='login')
def profile_page(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes was successfully saved ')
    context = {'form': form}
    return render(request, 'blog/profile_page.html', context)


def send_message(request):
    template = render_to_string('blog/email.html', {'name': request.user.username})

    email = EmailMessage(
        'Subject message',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email]
    )

    email.fail_silently = False
    email.send()

    return redirect('/')


def activate_account(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):

        user.customer.verified = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
