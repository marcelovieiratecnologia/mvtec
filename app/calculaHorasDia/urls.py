from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', calculaHorasExtras, name='calculaHorasExtras'),
    path('', calculoHorasExtrasPrimeiroPeriodo, name='calculoHorasExtrasPrimeiroPeriodo'),
    path('', calculoHorasExtrasSegundoPeriodo, name='calculoHorasExtrasSegundoPeriodo'),
]
