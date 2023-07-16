from django.shortcuts import redirect, render, get_object_or_404
from .models import Vacancy_pl, Application_pl
from django.contrib.auth.decorators import login_required


def index_pl(request):
    vacancies = Vacancy_pl.published.all()[:4]
    context = {'vacancies': vacancies}
    return render(request, 'vacancy_pl/index.html', context)


def vacancy_pl_detail(request, slug):
    vacancy = get_object_or_404(Vacancy_pl, slug=slug)
    context = {'vacancy': vacancy}
    return render(request, 'vacancy_pl/vacancy_detail.html', context)


def vacancy_pl_list(request):
    vacancies = Vacancy_pl.published.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancy_pl/list.html', context)


@login_required
def apply_to_vacancy_pl(request, vacancy_slug):
    vacancy = get_object_or_404(Vacancy_pl, slug=vacancy_slug)

    if request.method == 'POST':
        application = Application_pl()
        application.vacancy_pl = vacancy
        application.user = request.user
        application.name = request.POST.get('name')
        application.email = request.POST.get('email')
        application.phone = request.POST.get('phone')
        application.save()
        return redirect('vacancy_pl:vacancy_detail', slug=vacancy_slug)
    else:
        if request.user.is_authenticated:
            initial = {
                'name': request.user.first_name,
                'email': request.user.email,
                'phone': request.user.phone_number,
            }
        else:
            initial = {}

    return render(request, 'vacancy_pl/apply.html', {'vacancy': vacancy, 'initial': initial})
