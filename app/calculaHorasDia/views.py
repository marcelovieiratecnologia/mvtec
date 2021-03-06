from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.template.loader import render_to_string
import datetime

# Variáveis Globais
listaHrEntrada = []
listaHrSaidas = []

lsCalculaDifEntrada = []  # Lista que será adicionado as Diferenças da entrada
lsCalculaDifSaida = []  # Lista que será adicionado as Diferenças da Saída


class Calculo():
    def __init__(self, hrEntrada=0, hrChegada=0, listaHrChegadas=0, hrSaida=0, hrQueSaiu=0, listaHrSaidas=0):
        self.hrEntrada = hrEntrada
        self.hrChegada = hrChegada
        self.listaHrChegadas = listaHrChegadas
        self.hrSaida = hrSaida
        self.hrQueSaiu = hrQueSaiu
        self.listaHrSaidas = listaHrSaidas

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
    def hr_saida(self):
        return self.__hrSaida

    @hr_saida.setter
    def hr_saida(self, hrSai):
        self.__hrSaida = hrSai

    @property
    def lista_hr_chegadas(self):
        return self.__listaHrChegadas

    @lista_hr_chegadas.setter
    def lista_hr_chegadas(self, listaHrCheg):
        self.__listaHrChegadas = listaHrCheg

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

    # @@@@@@   CALCULA ENTRADA @@@@@@@
    # CALCULA A DIFERENÇA ENTRE A HORA QUE ENTRO COM AS HORAS QUE CHEGUEI E GUARDA EM UMA LISTA
    def calculo_horas_extras_antes_entradas(self, hrEntrada, listaHrChegadas):
        hrEntrada = str(hrEntrada)  # '08:30:00'  # Meu Horário de Entrada
        h, m, s = (map(int, hrEntrada.split(':')))
        HrEntrada = datetime.timedelta(0, s, 0, 0, m, h)

        # Lista com Horários que ENTREI mais CEDO na Empresa

        listHrChegadas = listaHrChegadas  # [hrChegada]   # ['07:30:00']
        # lsCalculaDifEntrada = []  # Lista que será adicionado as Diferenças da entrada

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
        # print('valor de l é :   ', l)
        somaEntrada.append(l)
        print('-------------------------------------------------------------------')
        print('|                     Calulando Horas Entradas                     |          ')
        print('-------------------------------------------------------------------|         |')
        print('Total de Horas Pagas que fiz antes das 08:30 até o momento foi de:  ', somaEntrada[0])
        print('-------------------------------------------------------------------|         |')
        print()
        print()
        return (somaEntrada[0])

    # @@@@@@   CALCULA SAIDA @@@@@@@
    # CALCULA A DIFERENÇA ENTRE A HORA QUE SAIO COM AS HORAS QUE SAÍ E GUARDA EM UMA LISTA
    def calculo_horas_extras_depois_saidas(self, hrSaida, listaHrSaidas):
        # Se estiver com valor '00:00:00' é por que não tive Horas extras depois das 17:30.
        if listaHrSaidas[0] != '00:00:00':
            hrSaida = str(hrSaida)  # '08:30:00'  # Meu Horário de Entrada
            h, m, s = (map(int, hrSaida.split(':')))
            HrSaida = datetime.timedelta(0, s, 0, 0, m, h)

            listHrSaidas = []
            listHrSaidas = listaHrSaidas

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

        # Se estiver com valor '00:00:00' é por que não tive Horas extras depois das 17:30.
        if listaHrSaidas[0] != '00:00:00':
            print('-------------------------------------------------------------------')
            print('|                     Calulando Horas Saídas                       |          ')
            print('-------------------------------------------------------------------|         |')
            print('Total de Horas Pagas que fiz depois das 17:30 até o momento foi de: ',
                  somaSaida[0], ' *** ##ANOTAÇÔES SAÍDAS:  ##***')
            print('-------------------------------------------------------------------|         |')
        return (somaSaida[0])


def calculo_horas_extras_primeiro_periodo(request):
    horariosChegadas = ''
    hrEntrada = ''
    hrChegada = ''

    # if 'edtListaAddChegadas' in request.GET:
    horariosChegadas = request.POST.get('edtListaAddChegadas', "")
    # if request.metho == 'GET':
    # 	# print(':::::::::::::', request.GET.get('edtListaAddChegadas'))
    # 	horariosChegadas = request.GET.get('edtListaAddChegadas')  # string que trago do front com todos os horarios
    # 	#print('Horarios de Chegada-------- : ', horariosChegadas)
    # else:
    # 	horariosChegadas = ''

    listaHrChegadas = horariosChegadas.split(',')  # convertendo em uma lista a string que trouxe do front

    # Referente ao calculo antes de começar a trabalhar
    if 'hrEntrada' in request.POST:
        hrEntrada = request.POST['hrEntrada']
    else:
        hrEntrada = ''
    if 'hrChegada' in request.POST:
        hrChegada = request.POST['hrChegada']
    else:
        hrChegada = ''

    if (hrEntrada != '') and (horariosChegadas != ''):  # and (hrChegada != ''):
        calculoHorasExtrasAntesEntradas = Calculo(
            hrEntrada, hrChegada, listaHrChegadas).calculo_horas_extras_antes_entradas(hrEntrada, listaHrChegadas)
    else:
        calculoHorasExtrasAntesEntradas = ''

    # return render(request,'calculaHorasDia/calculaHorasDia.html', {'hrEntrada':hrEntrada, 'hrChegada':hrChegada, 'calculoHorasExtrasAntesEntradas':calculoHorasExtrasAntesEntradas})
    return calculoHorasExtrasAntesEntradas


def calculo_horas_extras_segundo_periodo(request):

    if 'edtListaAddQueSaiu' in request.POST:
        horariosSaidas = request.POST.get('edtListaAddQueSaiu')  # string que trago do front com todos os horarios
        # print('Horarios de Saida: ', horariosSaidas)
    else:
        horariosSaidas = ''

    listaHrSaidas = horariosSaidas.split(',')
    # print(listaDeHorarios)

    # Referente ao calculo depois que saí do trabalho
    if 'hrSaida' in request.POST:
        hrSaida = request.POST['hrSaida']
    else:
        hrSaida = ''
    if 'hrQueSaiu' in request.POST:
        hrQueSaiu = request.POST['hrQueSaiu']
    else:
        hrQueSaiu = ''

    calculoHorasExtrasDepoisSaidas = ''
    if (hrSaida != '') and (horariosSaidas != ''):
        calculoHorasExtrasDepoisSaidas = Calculo(
            hrSaida, hrQueSaiu, listaHrSaidas).calculo_horas_extras_depois_saidas(hrSaida, listaHrSaidas)
    else:
        calculoHorasExtrasDepoisSaidas = ''

    # dic_CalcHrEnt_CalcHrSai = {}
    # if calculo_horas_extras_antes_entradas != '':
    # 	dic_CalcHrEnt_CalcHrSai['HrExtraEntrada'] = calculoHorasExtrasAntesEntradas
    # if calculo_horas_extras_depois_saidas != '':
    # 	dic_CalcHrEnt_CalcHrSai['HrExtraSaida'] = calculoHorasExtrasDepoisSaidas
    # print(dic_CalcHrEnt_CalcHrSai)

    # todo: Estou com o seguinte problema, se mando calcular atraveś do clique do botão , funciona certinho, mas se aperto o F5 , por mais que não tenha nenhum valor dentro dos inputs ele passa pela função e tras sei lá da onde o ultimo valor que adicionei e da um resoltado para o usuário
    # return render(request,'calculaHorasDia/calculaHorasDia.html', {'hrSaida':hrSaida, 'hrQueSaiu':hrQueSaiu, 'calculoHorasExtrasDepoisSaidas':calculoHorasExtrasDepoisSaidas})
    return calculoHorasExtrasDepoisSaidas


def calcula_horas_extras(request):
    url = request.META.get('HTTP_REFERER')
    rendered = render_to_string('calculaHorasDia/calculaHorasDia.html')
    calculoHorasPrimeiroPeriodo = 0
    calculoTotal = 0

    if request.method == 'POST':
        calculoHorasPrimeiroPeriodo = calculo_horas_extras_primeiro_periodo(request)
        # print('PRIMEIRO:::: ', calculoHorasPrimeiroPeriodo)

        # calculoHorasSegundoPeriodo = calculo_horas_extras_segundo_periodo(request)
        # print('SEGUNDO:::: ',calculoHorasSegundoPeriodo)
        #calculoTotal = calculoHorasPrimeiroPeriodo + calculoHorasSegundoPeriodo

        calculoTotal = calculoHorasPrimeiroPeriodo

        return render(request, 'calculaHorasDia/calculaHorasDia.html', {'calculoHorasPrimeiroPeriodo': calculoHorasPrimeiroPeriodo,
                                                                        # 															# 'calculoHorasSegundoPeriodo':calculoHorasSegundoPeriodo,
                                                                        'calculoTotal': calculoTotal})
    return render(request, 'calculaHorasDia/calculaHorasDia.html')
