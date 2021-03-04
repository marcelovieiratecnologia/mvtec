from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('calculaHorasDia/', TemplateView.as_view(template_name='calculaHorasDia/calculaHorasDia.html')),
    path('', calculaHorasExtras, name='calculaHorasExtras'),
    path('', calculoHorasExtrasPrimeiroPeriodo, name='calculoHorasExtrasPrimeiroPeriodo'),
    path('', calculoHorasExtrasSegundoPeriodo, name='calculoHorasExtrasSegundoPeriodo'),
]
