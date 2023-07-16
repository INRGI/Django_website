from django.contrib import admin
from .models import Vacancy_ru, City_ru, Application_ru


@admin.register(City_ru)
class City_ruAdmin(admin.ModelAdmin):
    list_display = ('cityname', 'slug')
    search_fields = ('cityname',)
    prepopulated_fields = {'slug': ('cityname',)}


class ApplicationInline(admin.TabularInline):
    model = Application_ru
    extra = 0


@admin.register(Vacancy_ru)
class Vacancy_ruAdmin(admin.ModelAdmin):
    list_display = ('vacancyname', 'city', 'slug', 'status')
    search_fields = ('vacancyname', 'description')
    list_filter = ('status', 'city')
    prepopulated_fields = {'slug': ('vacancyname',)}
    inlines = [ApplicationInline]


admin.site.register(Application_ru)
