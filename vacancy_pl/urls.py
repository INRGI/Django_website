from django.urls import path
from vacancy_pl import views

app_name = 'vacancy_pl'

urlpatterns = [
    path('', views.index_pl, name='index_pl'),
    path('vacancy/<slug:slug>/',
         views.vacancy_pl_detail, name='vacancy_detail'),
    path('vacancies/', views.vacancy_pl_list, name='vacancy_list'),
    path('vacancy/<slug:vacancy_slug>/apply/',
         views.apply_to_vacancy_pl, name='apply_pl'),
]
