from django.contrib import admin
from .models import Vacancy, City, Application


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('cityname', 'slug')
    search_fields = ('cityname',)
    prepopulated_fields = {'slug': ('cityname',)}


class ApplicationInline(admin.TabularInline):
    model = Application
    extra = 0


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('vacancyname', 'city', 'slug', 'status')
    search_fields = ('vacancyname', 'description')
    list_filter = ('status', 'city')
    prepopulated_fields = {'slug': ('vacancyname',)}
    inlines = [ApplicationInline]


admin.site.register(Application)
