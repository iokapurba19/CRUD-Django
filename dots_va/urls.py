from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.shortcuts import redirect
from dots_va.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('auth/', include(('authentication.urls', 'authentication'), namespace='authentication')),
    path('', lambda request: redirect('authentication:login')),
    path('dashboard/', include(('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('buku/', include(('buku.urls', 'buku'), namespace='buku')),
    path('grade/', include(('grade.urls', 'grade'), namespace='grade')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)