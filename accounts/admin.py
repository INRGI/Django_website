from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm

from .models import CustomUser, Pit


class PitInline(admin.TabularInline):
    model = Pit


class CustomUserAdmin(admin.ModelAdmin):
    inlines = [PitInline]
    list_display = ('username', 'first_name', 'last_name',
                    'is_staff', 'is_active')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Pit)
