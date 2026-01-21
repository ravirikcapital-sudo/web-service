from django.contrib import admin
from django.urls import path
from contact_page.views import contact_api 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_api, name='contact_api'),
    path('api/contact/', contact_api, name='contact_api'), 
]
