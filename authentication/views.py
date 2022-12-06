from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


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


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')