
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', lambda request: JsonResponse({"status": "API running"})),  # ✅ new root path
    path('admin/', admin.site.urls),
    path('api/users/', include('registration.urls')),
    path('api/', include('contact_page.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
