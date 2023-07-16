from django.db import models


class Vacancy_ruPublishedManager(models.Manager):
    def get_queryset(self):
        return (super(Vacancy_ruPublishedManager, self)
                .get_queryset()
                .filter(status='published'))
