from django.contrib import admin
from .models import Vacancy_pl, City_pl, Application_pl


@admin.register(City_pl)
class City_plAdmin(admin.ModelAdmin):
    list_display = ('cityname', 'slug')
    search_fields = ('cityname',)
    prepopulated_fields = {'slug': ('cityname',)}


class ApplicationInline(admin.TabularInline):
    model = Application_pl
    extra = 0


@admin.register(Vacancy_pl)
class Vacancy_plAdmin(admin.ModelAdmin):
    list_display = ('vacancyname', 'city', 'slug', 'status')
    search_fields = ('vacancyname', 'description')
    list_filter = ('status', 'city')
    prepopulated_fields = {'slug': ('vacancyname',)}
    inlines = [ApplicationInline]


admin.site.register(Application_pl)
