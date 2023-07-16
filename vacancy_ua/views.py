from django.shortcuts import redirect, render, get_object_or_404
from .models import Vacancy_ua, Application_ua
from django.contrib.auth.decorators import login_required


def index_ua(request):
    vacancies = Vacancy_ua.published.all()[:4]
    context = {'vacancies': vacancies}
    return render(request, 'vacancy_ua/index.html', context)


def vacancy_ua_detail(request, slug):
    vacancy = get_object_or_404(Vacancy_ua, slug=slug)
    context = {'vacancy': vacancy}
    return render(request, 'vacancy_ua/vacancy_detail.html', context)


def vacancy_ua_list(request):
    vacancies = Vacancy_ua.published.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy_ua/list.html', context)


@login_required
def apply_to_vacancy_ua(request, vacancy_slug):
    vacancy = get_object_or_404(Vacancy_ua, slug=vacancy_slug)

    if request.method == 'POST':
        application = Application_ua()
        application.vacancy_ua = vacancy
        application.user = request.user
        application.name = request.POST.get('name')
        application.email = request.POST.get('email')
        application.phone = request.POST.get('phone')
        application.save()
        return redirect('vacancy_ua:vacancy_detail', slug=vacancy_slug)
    else:
        if request.user.is_authenticated:
            initial = {
                'name': request.user.first_name,
                'email': request.user.email,
                'phone': request.user.phone_number,
            }
        else:
            initial = {}

    return render(request, 'vacancy_ua/apply.html', {'vacancy': vacancy, 'initial': initial})
