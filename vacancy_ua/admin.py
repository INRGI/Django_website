from django.contrib import admin
from .models import Vacancy_ua, City_ua, Application_ua


@admin.register(City_ua)
class City_uaAdmin(admin.ModelAdmin):
    list_display = ('cityname', 'slug')
    search_fields = ('cityname',)
    prepopulated_fields = {'slug': ('cityname',)}


class ApplicationInline(admin.TabularInline):
    model = Application_ua
    extra = 0


@admin.register(Vacancy_ua)
class Vacancy_uaAdmin(admin.ModelAdmin):
    list_display = ('vacancyname', 'city', 'slug', 'status')
    search_fields = ('vacancyname', 'description')
    list_filter = ('status', 'city')
    prepopulated_fields = {'slug': ('vacancyname',)}
    inlines = [ApplicationInline]


admin.site.register(Application_ua)
