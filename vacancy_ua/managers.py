from django.db import models


class Vacancy_uaPublishedManager(models.Manager):
    def get_queryset(self):
        return (super(Vacancy_uaPublishedManager, self)
                .get_queryset()
                .filter(status='published'))
