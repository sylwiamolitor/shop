from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout, get_user

from .models import Customer


def log_in(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("form = LoginForm(request.POST)")
        if form.is_valid():
            print("user = authenticate(")

            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                login(request, user)
                print("LOGGED IN")
                return redirect('index')
            else:
                context = {'form': form}
                return render(request, 'authentication/login.html', context)
        else:
            context = {'form': form}
            return render(request, 'authentication/login.html', context)

    else:
        context = {'form': LoginForm()}
        return render(request, 'authentication/login.html', context)


@login_required(login_url='/login')
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')


@transaction.atomic
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email')
            )
            customer = Customer(
                user=user,
                address1=form.cleaned_data.get('address_1'),
                address2=form.cleaned_data.get('address_2'),
                town_city=form.cleaned_data.get('town_city'),
                postcode=form.cleaned_data.get('postcode'),
                country=form.cleaned_data.get('country')
            )

            permissions = Permission.objects.filter(codename__in=['add_order', 'view_order', 'view_product'])
            user.user_permissions.set(permissions)

            user.save()
            customer.save()
            return redirect('/login')
        else:
            context = {'form': form}
            return render(request, 'authentication/signup.html', context)
    else:
        context = {'form': SignupForm()}
        return render(request, 'authentication/signup.html', context)


@login_required(login_url='/login')
def user_details(request):
    user = get_user(request)
    if not user.customer:
        return redirect('/')
    context = {'customer': user.customer}
    return render(request, 'authentication/userdetails.html', context)
