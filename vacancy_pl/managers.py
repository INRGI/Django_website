from django.db import models


class Vacancy_plPublishedManager(models.Manager):
    def get_queryset(self):
        return (super(Vacancy_plPublishedManager, self)
                .get_queryset()
                .filter(status='published'))
