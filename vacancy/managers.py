from django.db import models


class VacancyPublishedManager(models.Manager):
    def get_queryset(self):
        return (super(VacancyPublishedManager, self)
                .get_queryset()
                .filter(status='published'))

