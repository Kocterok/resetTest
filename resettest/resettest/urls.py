
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appreset.urls')),
    path('news/', include('news.urls')),
    path('calculator/', include('calculator.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
