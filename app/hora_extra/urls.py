from django.urls import path
from app.hora_extra import views as v


urlpatterns = [
    path('', v.hora_extra, name='hora_extra'),
    path(
        'primeiro-periodo/',
        v.calculo_hora_extra_primeiro_periodo,
        name='calculo_hora_extra_primeiro_periodo'
    ),
    path(
        'segundo-periodo/',
        v.calculo_hora_extra_segundo_periodo,
        name='calculo_hora_extra_segundo_periodo'
    ),
]
