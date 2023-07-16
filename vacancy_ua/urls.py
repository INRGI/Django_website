from django.urls import path
from vacancy_ua import views

app_name = 'vacancy_ua'

urlpatterns = [
    path('', views.index_ua, name='index_ua'),
    path('vacancy/<slug:slug>/', views.vacancy_ua_detail, name='vacancy_detail'),
    path('vacancies/', views.vacancy_ua_list, name='vacancy_list'),
    path('vacancy/<slug:vacancy_slug>/apply/',
         views.apply_to_vacancy_ua, name='apply_ua'),
]
