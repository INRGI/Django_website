from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Pit
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password1']
            pesel = form.cleaned_data['pesel']

            user = CustomUser.objects.create_user(
                email=email,
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                password=password,
                pesel=pesel
            )
            auth_login(request, user)
            return redirect('vacancy:index')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    # session expires when the user closes the browser
                    request.session.set_expiry(0)

                return redirect('vacancy:index')
            return redirect('vacancy:index')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('vacancy:index')


@login_required
def profile_view(request):
    pits = Pit.objects.filter(user=request.user)

    context = {
        'pits': pits,
    }
    return render(request, 'accounts/profile.html', context)
