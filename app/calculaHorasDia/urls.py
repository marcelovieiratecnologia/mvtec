from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    # path('calculaHorasDia/', TemplateView.as_view(template_name='calculaHorasDia/calculaHorasDia.html')),
    path('calcula-horas-extras/', calcula_horas_extras, name='calculaHorasExtras'),
    path('calculo-horas-extras-primeiro-periodo/', calculo_horas_extras_primeiro_periodo, name='calculoHorasExtrasPrimeiroPeriodo'),
    path('calculoHoras-extras-segundo-periodo/', calculo_horas_extras_segundo_periodo, name='calculoHorasExtrasSegundoPeriodo'),
]
