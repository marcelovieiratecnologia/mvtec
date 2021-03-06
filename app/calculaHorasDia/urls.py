from django.urls import path
from mvtec.app.calcula_horas_dia import views as v
from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name='calculaHorasDia/calculaHorasDia.html'), name='calcula_horas_extras'),
    path('', v.calculo_horas_extras, name='calcula_horas_extras'),
    path('calcula-horas-extras/', calcula_horas_extras),
    path('calculo-horas-extras-primeiro-periodo/', calculo_horas_extras_primeiro_periodo,
         name='calculoHorasExtrasPrimeiroPeriodo'),
    path('calculoHoras-extras-segundo-periodo/', calculo_horas_extras_segundo_periodo, name='calculoHorasExtrasSegundoPeriodo'),
]
