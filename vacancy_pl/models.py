from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

from .managers import Vacancy_plPublishedManager

User = get_user_model()


class City_pl(models.Model):
    cityname = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'cities'
        ordering = ('cityname',)

    def __str__(self):
        return self.cityname


class Vacancy_pl(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    vacancyname = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200, blank=True)
    description = models.TextField()
    profession = models.CharField(max_length=200)
    payment = models.CharField(max_length=200)
    housing = models.CharField(max_length=200)
    work_schedule = models.CharField(max_length=200)
    additional_services = models.CharField(max_length=200)
    image = models.ImageField(upload_to='vacancy_images', blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    city = models.ForeignKey(City_pl,
                             on_delete=models.CASCADE,
                             related_name='vacancies_pl')

    objects = models.Manager()
    published = Vacancy_plPublishedManager()

    applications = models.ManyToManyField(User, through='Application_pl', related_name='vacancies_pl_applied')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.vacancyname)
            # Перевірка на унікальність slug
            counter = 1
            while Vacancy_pl.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.vacancyname) + '-' + str(counter)
                counter += 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('vacancyname',)
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.vacancyname

    def get_absolute_url(self):
        return reverse('vacancy_pl:vacancy_detail',
                       args=[self.slug])

class Application_pl(models.Model):
    vacancy_pl = models.ForeignKey(Vacancy_pl, on_delete=models.CASCADE, related_name='application_pl_set')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Application for {self.vacancy_pl.vacancyname} by {self.user.username}" if self.user else f"Application for {self.vacancy_pl.vacancyname}"

    def get_absolute_url(self):
        return reverse('vacancy_pl:application_detail', args=[self.pk])

