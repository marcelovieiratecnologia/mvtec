from django.urls import path
from app.calcula_horas_dia import views as v
from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='calculaHorasDia/calculaHorasDia.html'), name='calcula_horas_extras'),
    path('', v.calculo_horas_extras, name='calcula_horas_extras'),
    path('calculo-horas-extras/', v.calcula_horas_extras),
    path(
        'calculo-horas-extras-primeiro-periodo/',
        v.calculo_horas_extras_primeiro_periodo,
        name='calculoHorasExtrasPrimeiroPeriodo'
    ),
    path(
        'calculo-horas-extras-segundo-periodo/',
        v.calculo_horas_extras_segundo_periodo,
        name='calculoHorasExtrasSegundoPeriodo'
    ),
]
