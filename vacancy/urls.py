from django.urls import path
from vacancy import views

app_name = 'vacancy'

urlpatterns = [
    path('', views.index, name='index'),
    path('vacancy/<slug:slug>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('vacancy/<slug:vacancy_slug>/apply/',
         views.apply_to_vacancy, name='apply'),
]
