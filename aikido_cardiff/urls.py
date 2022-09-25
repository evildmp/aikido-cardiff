from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import aikido_cardiff.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("favicon.ico", aikido_cardiff.views.favicon),
]

if settings.DEBUG:
    urlpatterns.extend(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

urlpatterns.append(path('', include('cms.urls')))
