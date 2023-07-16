from django.contrib.auth import get_user_model, login as auth_login, logout as auth_logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Pit
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserForgotPasswordForm, UserSetNewPasswordForm


User = get_user_model()


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_username = form.cleaned_data.get('username')
            username = EmailMessage(
                mail_subject, message, to=[to_username]
            )
            username.send()
            return render(request, 'accounts/login.html')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)  # Зміна імені функції login на auth_login
        return redirect('vacancy:index')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
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


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    form_class = UserForgotPasswordForm
    template_name = 'accounts/user_password_reset.html'
    success_url = reverse_lazy('vacancy:index')
    success_message = "A letter with instructions for password recovery has been sent to your email"
    subject_template_name = 'accounts/email/password_subject_reset_mail.txt'
    email_template_name = 'accounts/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Password reset request'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = UserSetNewPasswordForm
    template_name = 'accounts/user_password_set_new.html'
    success_url = reverse_lazy('vacancy:index')
    success_message = 'The password has been successfully changed.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Set a new password'
        return context

# PL


def register_view_pl(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('accounts_pl/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_username = form.cleaned_data.get('username')
            username = EmailMessage(
                mail_subject, message, to=[to_username]
            )
            username.send()
            return render(request, 'accounts_pl/login.html')
    else:
        form = RegistrationForm()
    return render(request, 'accounts_pl/registration.html', {'form': form})


def activate_pl(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)  # Зміна імені функції login на auth_login
        return redirect('vacancy_pl:index_pl')


def login_view_pl(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    request.session.set_expiry(0)

                return redirect('vacancy_pl:index_pl')

            return redirect('vacancy_pl:index_pl')
    else:
        form = LoginForm()

    return render(request, 'accounts_pl/login.html', {'form': form})


def logout_view_pl(request):
    auth_logout(request)
    return redirect('vacancy_pl:index_pl')


@login_required
def profile_view_pl(request):
    pits = Pit.objects.filter(user=request.user)

    context = {
        'pits': pits,
    }
    return render(request, 'accounts_pl/profile.html', context)


class UserForgotPasswordView_pl(SuccessMessageMixin, PasswordResetView):
    form_class = UserForgotPasswordForm
    template_name = 'accounts_pl/user_password_reset.html'
    success_url = reverse_lazy('vacancy_pl:index_pl')
    success_message = "A letter with instructions for password recovery has been sent to your email"
    subject_template_name = 'accounts_pl/email/password_subject_reset_mail.txt'
    email_template_name = 'accounts_pl/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Password reset request'
        return context


class UserPasswordResetConfirmView_pl(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = UserSetNewPasswordForm
    template_name = 'accounts_pl/user_password_set_new.html'
    success_url = reverse_lazy('vacancy_pl:index_pl')
    success_message = 'The password has been successfully changed. You can log in on the site.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Set a new password'
        return context

# RU


def register_view_ru(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('accounts_ru/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_username = form.cleaned_data.get('username')
            username = EmailMessage(
                mail_subject, message, to=[to_username]
            )
            username.send()
            return render(request, 'accounts_ru/login.html')
    else:
        form = RegistrationForm()
    return render(request, 'accounts_ru/registration.html', {'form': form})


def activate_ru(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        return redirect('vacancy_ru:index_pl')


def login_view_ru(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    request.session.set_expiry(0)

                return redirect('vacancy_ru:index_ru')

            return redirect('vacancy_ru:index_ru')
    else:
        form = LoginForm()

    return render(request, 'accounts_ru/login.html', {'form': form})


def logout_view_ru(request):
    auth_logout(request)
    return redirect('vacancy_ru:index_ru')


@login_required
def profile_view_ru(request):
    pits = Pit.objects.filter(user=request.user)

    context = {
        'pits': pits,
    }
    return render(request, 'accounts_ru/profile.html', context)


class UserForgotPasswordView_ru(SuccessMessageMixin, PasswordResetView):
    form_class = UserForgotPasswordForm
    template_name = 'accounts_ru/user_password_reset.html'
    success_url = reverse_lazy('vacancy_ru:index_ru')
    success_message = "A letter with instructions for password recovery has been sent to your email"
    subject_template_name = 'accounts_ru/email/password_subject_reset_mail.txt'
    email_template_name = 'accounts_ru/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Password reset request'
        return context


class UserPasswordResetConfirmView_ru(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = UserSetNewPasswordForm
    template_name = 'accounts_ru/user_password_set_new.html'
    success_url = reverse_lazy('vacancy_ru:index_ru')
    success_message = 'The password has been successfully changed. You can log in on the site.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Set a new password'
        return context

# UA


def register_view_ua(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('accounts_ua/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_username = form.cleaned_data.get('username')
            username = EmailMessage(
                mail_subject, message, to=[to_username]
            )
            username.send()
            return render(request, 'accounts_ua/login.html')
    else:
        form = RegistrationForm()
    return render(request, 'accounts_ua/registration.html', {'form': form})


def activate_ua(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        return redirect('vacancy_ua:index_ua')


def login_view_ua(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    request.session.set_expiry(0)

                return redirect('vacancy_ua:index_ua')

            return redirect('vacancy_ua:index_ua')
    else:
        form = LoginForm()

    return render(request, 'accounts_ua/login.html', {'form': form})


def logout_view_ua(request):
    auth_logout(request)
    return redirect('vacancy_ua:index_ua')


@login_required
def profile_view_ua(request):
    pits = Pit.objects.filter(user=request.user)

    context = {
        'pits': pits,
    }
    return render(request, 'accounts_ua/profile.html', context)


class UserForgotPasswordView_ua(SuccessMessageMixin, PasswordResetView):
    form_class = UserForgotPasswordForm
    template_name = 'accounts_ua/user_password_reset.html'
    success_url = reverse_lazy('vacancy_ua:index_ua')
    success_message = "A letter with instructions for password recovery has been sent to your email"
    subject_template_name = 'accounts_ua/email/password_subject_reset_mail.txt'
    email_template_name = 'accounts_ua/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Password reset request'
        return context


class UserPasswordResetConfirmView_ua(SuccessMessageMixin, PasswordResetConfirmView):
    form_class = UserSetNewPasswordForm
    template_name = 'accounts_ru/user_password_set_new.html'
    success_url = reverse_lazy('vacancy_ua:index_ua')
    success_message = 'The password has been successfully changed. You can log in on the site.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Set a new password'
        return context
