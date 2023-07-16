from django.urls import path
from vacancy_ru import views

app_name = 'vacancy_ru'

urlpatterns = [
    path('', views.index_ru, name='index_ru'),
    path('vacancy/<slug:slug>/', views.vacancy_ru_detail, name='vacancy_detail'),
    path('vacancies/', views.vacancy_ru_list, name='vacancy_list'),
    path('vacancy/<slug:vacancy_slug>/apply/',
         views.apply_to_vacancy_ru, name='apply_ru'),
]
