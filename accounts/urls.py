from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import activate, activate_pl
from .views import UserForgotPasswordView, UserForgotPasswordView_ru, UserForgotPasswordView_ua, UserPasswordResetConfirmView, UserForgotPasswordView_pl, UserPasswordResetConfirmView_pl, UserPasswordResetConfirmView_ru, UserPasswordResetConfirmView_ua

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/',
         UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # PL
    path('pl/register/', views.register_view_pl, name='register_pl'),
    path('pl/login/', views.login_view_pl, name='login_pl'),
    path('pl/logout/', views.logout_view_pl, name='logout_pl'),
    path('pl/profile/', views.profile_view_pl, name='profile_pl'),
    path('pl/activate/<uidb64>/<token>/',
         views.activate_pl, name='activate_pl'),
    path('pl/password-reset/', UserForgotPasswordView_pl.as_view(),
         name='password_reset_pl'),
    path('pl/set-new-password/<uidb64>/<token>/',
         UserPasswordResetConfirmView_pl.as_view(), name='password_reset_confirm_pl'),
    # RU
    path('ru/register/', views.register_view_ru, name='register_ru'),
    path('ru/login/', views.login_view_ru, name='login_ru'),
    path('ru/logout/', views.logout_view_ru, name='logout_ru'),
    path('ru/profile/', views.profile_view_ru, name='profile_ru'),
    path('ru/activate/<uidb64>/<token>/',
         views.activate_ru, name='activate_ru'),
    path('ru/password-reset/', UserForgotPasswordView_ru.as_view(),
         name='password_reset_ru'),
    path('ru/set-new-password/<uidb64>/<token>/',
         UserPasswordResetConfirmView_ru.as_view(), name='password_reset_confirm_ru'),
    # UA
    path('ua/register/', views.register_view_ua, name='register_ua'),
    path('ua/login/', views.login_view_ua, name='login_ua'),
    path('ua/logout/', views.logout_view_ua, name='logout_ua'),
    path('ua/profile/', views.profile_view_ua, name='profile_ua'),
    path('ua/activate/<uidb64>/<token>/',
         views.activate_ua, name='activate_ua'),
    path('ua/password-reset/', UserForgotPasswordView_ua.as_view(),
         name='password_reset_ua'),
    path('ua/set-new-password/<uidb64>/<token>/',
         UserPasswordResetConfirmView_ua.as_view(), name='password_reset_confirm_ua'),
]
