from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('politica_privacidade/', politica_privacidade, name='politica_privacidade'),
    path('termos_uso/', termos_uso, name='termos_uso'),

]
