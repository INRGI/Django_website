from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

from .managers import Vacancy_uaPublishedManager

User = get_user_model()


class City_ua(models.Model):
    cityname = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'cities'
        ordering = ('cityname',)

    def __str__(self):
        return self.cityname


class Vacancy_ua(models.Model):
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
    city = models.ForeignKey(City_ua,
                             on_delete=models.CASCADE,
                             related_name='vacancies_ua')

    objects = models.Manager()
    published = Vacancy_uaPublishedManager()

    applications = models.ManyToManyField(User, through='Application_ua', related_name='vacancies_ua_applied')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.vacancyname)
            # Перевірка на унікальність slug
            counter = 1
            while Vacancy_ua.objects.filter(slug=self.slug).exists():
                self.slug = slugify(self.vacancyname) + '-' + str(counter)
                counter += 1
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('vacancyname',)
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return self.vacancyname

    def get_absolute_url(self):
        return reverse('vacancy_ua:vacancy_detail',
                       args=[self.slug])

class Application_ua(models.Model):
    vacancy_ua = models.ForeignKey(Vacancy_ua, on_delete=models.CASCADE, related_name='application_ua_set')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Application for {self.vacancy_ua.vacancyname} by {self.user.username}" if self.user else f"Application for {self.vacancy_ua.vacancyname}"

    def get_absolute_url(self):
        return reverse('vacancy_ua:application_detail', args=[self.pk])

