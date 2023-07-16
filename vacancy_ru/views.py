from django.shortcuts import redirect, render, get_object_or_404
from .models import Vacancy_ru, Application_ru
from django.contrib.auth.decorators import login_required


def index_ru(request):
    vacancies = Vacancy_ru.published.all()[:4]
    context = {'vacancies': vacancies}
    return render(request, 'vacancy_ru/index.html', context)


def vacancy_ru_detail(request, slug):
    vacancy = get_object_or_404(Vacancy_ru, slug=slug)
    context = {'vacancy': vacancy}
    return render(request, 'vacancy_ru/vacancy_detail.html', context)


def vacancy_ru_list(request):
    vacancies = Vacancy_ru.published.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy_ru/list.html', context)


@login_required
def apply_to_vacancy_ru(request, vacancy_slug):
    vacancy = get_object_or_404(Vacancy_ru, slug=vacancy_slug)

    if request.method == 'POST':
        application = Application_ru()
        application.vacancy_ru = vacancy
        application.user = request.user
        application.name = request.POST.get('name')
        application.email = request.POST.get('email')
        application.phone = request.POST.get('phone')
        application.save()
        return redirect('vacancy_ru:vacancy_detail', slug=vacancy_slug)
    else:
        if request.user.is_authenticated:
            initial = {
                'name': request.user.first_name,
                'email': request.user.email,
                'phone': request.user.phone_number,
            }
        else:
            initial = {}

    return render(request, 'vacancy_ru/apply.html', {'vacancy': vacancy, 'initial': initial})
