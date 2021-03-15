import datetime
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.template.loader import render_to_string

# Variáveis Globais
# listaHrEntrada = []
# listaHrSaidas = []

# lsCalculaDifEntrada = []  # Lista que será adicionado as Diferenças da entrada
# lsCalculaDifSaida = []  # Lista que será adicionado as Diferenças da Saída


def timedelta_to_string(value, format='%H:%M'):
    '''
    Transforma timedelta em string no formato %H:%M.
    '''
    return datetime.datetime.strftime(datetime.datetime.strptime(str(value), '%H:%M:%S'), '%H:%M')


def hora_extra(request):
    template_name = 'hora_extra/hora_extra.html'
    return render(request, template_name)


# class Calculo():
#     def __init__(self, hrEntrada=0, hrChegada=0, listaHrChegadas=0, hrSaida=0, hrQueSaiu=0, listaHrSaidas=0):
#         self.hrEntrada = hrEntrada
#         self.hrChegada = hrChegada
#         self.listaHrChegadas = listaHrChegadas
#         self.hrSaida = hrSaida
#         self.hrQueSaiu = hrQueSaiu
#         self.listaHrSaidas = listaHrSaidas
#
#     @property
#     def hr_entrada(self):
#         return self.__hrEntrada
#
#     @hr_entrada.setter
#     def hr_entrada(self, hrEnt):
#         self.__hrEntrada = hrEnt
#
#     @property
#     def hr_chegada(self):
#         return self.__hrChegada
#
#     @hr_chegada.setter
#     def hr_chegada(self, hrCheg):
#         self.__hrChegada = hrCheg
#
#     @property
#     def lista_hr_chegadas(self):
#         return self.__listaHrChegadas
#
#     @lista_hr_chegadas.setter
#     def lista_hr_chegadas(self, listaHrCheg):
#         self.__listaHrChegadas = listaHrCheg
#
#     @property
#     def hr_saida(self):
#         return self.__hrSaida
#
#     @hr_saida.setter
#     def hr_saida(self, hrSai):
#         self.__hrSaida = hrSai
#
#     @property
#     def hr_que_saiu(self):
#         return self.__hrQueSaiu
#
#     @hr_que_saiu.setter
#     def hr_que_saiu(self, hrQueSai):
#         self.__hrQueSaiu = hrQueSai
#
#     @property
#     def lista_hr_saidas(self):
#         return self.__listaHrSaidas
#
#     @lista_hr_saidas.setter
#     def lista_hr_saidas(self, listaHrSai):
#         self.__listaHrSaidas = listaHrSai
#
#     # @@@@@@   CALCULA ENTRADA @@@@@@@
#     # CALCULA A DIFERENÇA ENTRE A HORA QUE ENTRO COM AS HORAS QUE CHEGUEI E GUARDA EM UMA LISTA
#     def calculo_horas_extras_antes_entradas(self):
#         hrEntrada = str(self.hrEntrada)  # '08:30:00'  # Meu Horário de Entrada
#         h, m, s = (map(int, hrEntrada.split(':')))
#         HrEntrada = datetime.timedelta(0, s, 0, 0, m, h)
#
#         # Lista com Horários que ENTREI mais CEDO na Empresa
#         listHrChegadas = self.listaHrChegadas  # [hrChegada]   # ['07:30:00']
#         lsCalculaDifEntrada = []  # Lista que será adicionado as Diferenças da entrada
#
#         HrBanco = []  # Lista que será adicionado as Diferenças
#
#         for lhoras in listHrChegadas:
#             # Encontrando a diferença entre as horas
#             h, m, s = (map(int, lhoras.split(':')))
#             lhoras = datetime.timedelta(0, s, 0, 0, m, h)
#             # print('type variável horas: ',type(horas))
#             Dif = HrEntrada - lhoras
#             # print('Total é :', Dif )
#             lsCalculaDifEntrada.append(Dif)
#
#         somaEntrada = []
#         tam = len(lsCalculaDifEntrada)
#         # print(tam)
#         x = 0
#         while x < tam:
#             # print(x)
#             if x == 0:
#                 l = lsCalculaDifEntrada[x]
#             if x > 0:
#                 l += +lsCalculaDifEntrada[x]
#             x += 1
#
#         somaEntrada.append(l)
#         return (somaEntrada[0])
#
#     # @@@@@@   CALCULA SAIDA @@@@@@@
#     # CALCULA A DIFERENÇA ENTRE A HORA QUE SAIO COM AS HORAS QUE SAÍ E GUARDA EM UMA LISTA
#     def calculo_horas_extras_depois_saidas(self):
#
#         hrSaida = str(self.hrSaida)  # '08:30:00'  # Meu Horário de Saída
#         h, m, s = (map(int, hrSaida.split(':')))
#         HrSaida = datetime.timedelta(0, s, 0, 0, m, h)
#
#         listHrSaidas = self.listaHrSaidas
#         lsCalculaDifSaida = []
#
#         for lhoras in listHrSaidas:
#             # Encontrando a diferença entre as horas
#             h, m, s = (map(int, lhoras.split(':')))
#             lhoras = datetime.timedelta(0, s, 0, 0, m, h)
#             # print('type variável horas: ',type(horas))
#             Dif = lhoras - HrSaida
#             # print('Total é :', Dif )
#             lsCalculaDifSaida.append(Dif)
#
#         somaSaida = []
#         tam = len(lsCalculaDifSaida)
#         # print(tam)
#         x = 0
#         while x < tam:
#             # print(x)
#             if x == 0:
#                 l = lsCalculaDifSaida[x]
#             if x > 0:
#                 l += +lsCalculaDifSaida[x]
#             x += 1
#         # print('valor de l é :   ', l)
#         somaSaida.append(l)
#         return (somaSaida[0])


class CalculoPrimeiroPeriodo():
    def __init__(self, hrEntrada=0, hrChegada=0, listaHrChegadas=0):
        self.hrEntrada = hrEntrada
        self.hrChegada = hrChegada
        self.listaHrChegadas = listaHrChegadas

    @property
    def hr_entrada(self):
        return self.__hrEntrada

    @hr_entrada.setter
    def hr_entrada(self, hrEnt):
        self.__hrEntrada = hrEnt

    @property
    def hr_chegada(self):
        return self.__hrChegada

    @hr_chegada.setter
    def hr_chegada(self, hrCheg):
        self.__hrChegada = hrCheg

    @property
    def lista_hr_chegadas(self):
        return self.__listaHrChegadas

    @lista_hr_chegadas.setter
    def lista_hr_chegadas(self, listaHrCheg):
        self.__listaHrChegadas = listaHrCheg

    # @@@@@@   CALCULA ENTRADA @@@@@@@
    # CALCULA A DIFERENÇA ENTRE A HORA QUE ENTRO COM AS HORAS QUE CHEGUEI E GUARDA EM UMA LISTA
    def calculo_horas_extras_antes_entradas(self):
        hrEntrada = str(self.hrEntrada)  # '08:30:00'  # Meu Horário de Entrada
        h, m, s = (map(int, hrEntrada.split(':')))
        HrEntrada = datetime.timedelta(0, s, 0, 0, m, h)

        # Lista com Horários que ENTREI mais CEDO na Empresa
        listHrChegadas = self.listaHrChegadas  # [hrChegada]   # ['07:30:00']
        lsCalculaDifEntrada = []  # Lista que será adicionado as Diferenças da entrada

        HrBanco = []  # Lista que será adicionado as Diferenças

        for lhoras in listHrChegadas:
            # Encontrando a diferença entre as horas
            h, m, s = (map(int, lhoras.split(':')))
            lhoras = datetime.timedelta(0, s, 0, 0, m, h)
            # print('type variável horas: ',type(horas))
            Dif = HrEntrada - lhoras
            # print('Total é :', Dif )
            lsCalculaDifEntrada.append(Dif)

        somaEntrada = []
        tam = len(lsCalculaDifEntrada)
        # print(tam)
        x = 0
        while x < tam:
            # print(x)
            if x == 0:
                l = lsCalculaDifEntrada[x]
            if x > 0:
                l += +lsCalculaDifEntrada[x]
            x += 1

        somaEntrada.append(l)
        return (somaEntrada[0])


class CalculoSegundoPeriodo():
    def __init__(self, hrSaida=0, hrQueSaiu=0, listaHrSaidas=0):
        self.hrSaida = hrSaida
        self.hrQueSaiu = hrQueSaiu
        self.listaHrSaidas = listaHrSaidas

    @property
    def hr_saida(self):
        return self.__hrSaida

    @hr_saida.setter
    def hr_saida(self, hrSai):
        self.__hrSaida = hrSai

    @property
    def hr_que_saiu(self):
        return self.__hrQueSaiu

    @hr_que_saiu.setter
    def hr_que_saiu(self, hrQueSai):
        self.__hrQueSaiu = hrQueSai

    @property
    def lista_hr_saidas(self):
        return self.__listaHrSaidas

    @lista_hr_saidas.setter
    def lista_hr_saidas(self, listaHrSai):
        self.__listaHrSaidas = listaHrSai

    # @@@@@@   CALCULA SAIDA @@@@@@@
    # CALCULA A DIFERENÇA ENTRE A HORA QUE SAIO COM AS HORAS QUE SAÍ E GUARDA EM UMA LISTA
    def calculo_horas_extras_depois_saidas(self):
        hrSaida = str(self.hrSaida)  # '08:30:00'  # Meu Horário de Saída
        h, m, s = (map(int, hrSaida.split(':')))
        HrSaida = datetime.timedelta(0, s, 0, 0, m, h)

        listHrSaidas = self.listaHrSaidas
        lsCalculaDifSaida = []

        for lhoras in listHrSaidas:
            # Encontrando a diferença entre as horas
            h, m, s = (map(int, lhoras.split(':')))
            lhoras = datetime.timedelta(0, s, 0, 0, m, h)
            # print('type variável horas: ',type(horas))
            Dif = lhoras - HrSaida
            # print('Total é :', Dif )
            lsCalculaDifSaida.append(Dif)

        somaSaida = []
        tam = len(lsCalculaDifSaida)
        # print(tam)
        x = 0
        while x < tam:
            # print(x)
            if x == 0:
                l = lsCalculaDifSaida[x]
            if x > 0:
                l += +lsCalculaDifSaida[x]
            x += 1
        # print('valor de l é :   ', l)
        somaSaida.append(l)
        return (somaSaida[0])


def calcula_hora_extra(request):
    # print(request.POST)
    if request.method == 'POST':
        entrada = request.POST.get('hrEntrada')
        lista_add_chegadas = request.POST.get('edtListaAddChegadas')

        saida = request.POST.get('hrSaida')
        lista_add_saidas = request.POST.get('edtListaAddQueSaiu')

        hora_extra_primeiro_periodo = calculo_hora_extra_primeiro_periodo(entrada, lista_add_chegadas)
        hora_extra_segundo_periodo = calculo_hora_extra_segundo_periodo(saida, lista_add_saidas)

        total = hora_extra_primeiro_periodo  + hora_extra_segundo_periodo

        data = {
            'hora_extra_primeiro_periodo': timedelta_to_string(hora_extra_primeiro_periodo),
            'hora_extra_segundo_periodo': timedelta_to_string(hora_extra_segundo_periodo),
            'total': timedelta_to_string(total),
        }
        return JsonResponse(data)

    return JsonResponse({})


def calculo_hora_extra_primeiro_periodo(entrada, lista_add_chegadas):
    # horarios_chegadas = ''
    # hrEntrada = ''
    hrChegada = ''

    horarios_chegadas = lista_add_chegadas

    listaHrChegadas = horarios_chegadas.split(',')  # convertendo em uma lista a string que trouxe do front

    # Referente ao calculo antes de começar a trabalhar
    hrEntrada = entrada

    if (hrEntrada != '') and (horarios_chegadas != ''):
        # calculo = Calculo(hrEntrada, hrChegada, listaHrChegadas)
        # calculoHorasExtrasAntesEntradas = calculo.calculo_horas_extras_antes_entradas()
        calculo_primeiro_periodo = CalculoPrimeiroPeriodo(hrEntrada, hrChegada, listaHrChegadas)
        calculoHorasExtrasAntesEntradas = calculo_primeiro_periodo.calculo_horas_extras_antes_entradas()
    else:
        calculoHorasExtrasAntesEntradas = ''

    return calculoHorasExtrasAntesEntradas


def calculo_hora_extra_segundo_periodo(saida, lista_add_saidas):
    # horarios_saidas = ''
    # hrSaida = ''
    hrQueSaiu = ''

    horarios_saidas = lista_add_saidas

    listaHrSaidas = horarios_saidas.split(',')
    # print(listaDeHorarios)

    hrSaida = saida

    if (hrSaida != '') and (horarios_saidas != ''):
        # calculoHorasExtrasDepoisSaidas = Calculo(hrSaida, hrQueSaiu, listaHrSaidas).calculo_horas_extras_depois_saidas(hrSaida, listaHrSaidas)
        #TODO: Ver essa variavel hrSaida e listaHrSaidas que qdo entra no ojbeto ela perde o valor
        # calculo = Calculo(hrSaida, hrQueSaiu, listaHrSaidas)
        # calculoHorasExtrasDepoisSaidas = calculo.calculo_horas_extras_depois_saidas()
        calculo_segundo_periodo = CalculoSegundoPeriodo(hrSaida, hrQueSaiu, listaHrSaidas)
        calculoHorasExtrasDepoisSaidas = calculo_segundo_periodo.calculo_horas_extras_depois_saidas()

    else:
        calculoHorasExtrasDepoisSaidas = ''

    return calculoHorasExtrasDepoisSaidas
