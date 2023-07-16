from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('vacancy.urls', namespace='vacancy')),
    path('pl/', include('vacancy_pl.urls', namespace='vacancy_pl')),
    path('ru/', include('vacancy_ru.urls', namespace='vacancy_ru')),
    path('ua/', include('vacancy_ua.urls', namespace='vacancy_ua')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
