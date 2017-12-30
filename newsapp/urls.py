from django.urls import path

from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('investing/<int:year>/<int:month>/<int:day>/<str:slug>', views.investing, name='investing')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)