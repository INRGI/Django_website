from django.shortcuts import redirect, render, get_object_or_404
from .models import Vacancy, Application
from django.contrib.auth.decorators import login_required


def index(request):
    vacancies = Vacancy.published.all()[:4]
    context = {'vacancies': vacancies}
    return render(request, 'vacancy/index.html', context)


def vacancy_detail(request, slug):
    vacancy = get_object_or_404(Vacancy, slug=slug)
    context = {'vacancy': vacancy}
    return render(request, 'vacancy/vacancy_detail.html', context)


def vacancy_list(request):
    vacancies = Vacancy.published.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy/list.html', context)


@login_required
def apply_to_vacancy(request, vacancy_slug):
    vacancy = get_object_or_404(Vacancy, slug=vacancy_slug)

    if request.method == 'POST':
        application = Application()
        application.vacancy = vacancy
        application.user = request.user  # Передача авторизованого користувача
        application.name = request.POST.get('name')
        application.email = request.POST.get('email')
        application.phone = request.POST.get('phone')
        application.save()
        return redirect('vacancy:vacancy_detail', slug=vacancy_slug)
    else:
        if request.user.is_authenticated:
            initial = {
                'name': request.user.first_name,
                'email': request.user.email,
                'phone': request.user.phone_number,
            }
        else:
            initial = {}

    return render(request, 'vacancy/apply.html', {'vacancy': vacancy, 'initial': initial})

