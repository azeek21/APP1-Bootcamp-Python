from django.urls import path, include
from .views import test
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('', test),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)