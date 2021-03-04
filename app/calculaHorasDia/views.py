from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
import datetime

# Variáveis Globais
listaHrEntrada = []
listaHrSaidas = []

lsCalculaDifEntrada = [] # Lista que será adicionado as Diferenças da entrada
lsCalculaDifSaida = [] # Lista que será adicionado as Diferenças da Saída

class calculo():
	def __init__(self, hrEntrada=0, hrChegada=0, listaHrChegadas=0, hrSaida=0, hrQueSaiu=0, listaHrSaidas=0):
		self.hrEntrada = hrEntrada
		self.hrChegada = hrChegada
		self.listaHrChegadas = listaHrChegadas
		self.hrSaida = hrSaida
		self.hrQueSaiu = hrQueSaiu
		self.listaHrSaidas = listaHrSaidas

	@property
	def hrEntrada(self):
		return self.__hrEntrada
	@hrEntrada.setter
	def hrEntrada(self, hrEnt):
		self.__hrEntrada = hrEnt

	@property
	def hrChegada(self):
		return self.__hrChegada
	@hrChegada.setter
	def hrChegada(self, hrCheg):
		self.__hrChegada = hrCheg

	@property
	def hrSaida(self):
		return self.__hrSaida
	@hrSaida.setter
	def hrSaida(self, hrSai):
		self.__hrSaida = hrSai

	@property
	def listaHrChegadas(self):
		return self.__listaHrChegadas
	@listaHrChegadas.setter
	def listaHrChegadas(self, listaHrCheg):
		self.__listaHrChegadas = listaHrCheg

	@property
	def hrSaida(self):
		return self.__hrSaida
	@hrSaida.setter
	def hrSaida(self, hrSai):
		self.__hrSaida = hrSai

	@property
	def hrQueSaiu(self):
		return self.__hrQueSaiu
	@hrQueSaiu.setter
	def hrQueSaiu(self, hrQueSai):
		self.__hrQueSaiu = hrQueSai

	@property
	def listaHrSaidas(self):
		return self.__listaHrSaidas
	@listaHrSaidas.setter
	def listaHrSaidas(self, listaHrSai):
		self.__listaHrSaidas = listaHrSai

	# @@@@@@   CALCULA ENTRADA @@@@@@@
	# CALCULA A DIFERENÇA ENTRE A HORA QUE ENTRO COM AS HORAS QUE CHEGUEI E GUARDA EM UMA LISTA
	def calculoHorasExtrasAntesEntradas(self, hrEntrada, listaHrChegadas):
		hrEntrada = str(hrEntrada) # '08:30:00'  # Meu Horário de Entrada
		h, m, s = (map(int, hrEntrada.split(':')))
		HrEntrada = datetime.timedelta(0, s, 0, 0, m, h)

		# Lista com Horários que ENTREI mais CEDO na Empresa

		listHrChegadas =  listaHrChegadas  # [hrChegada]   # ['07:30:00']
		#lsCalculaDifEntrada = []  # Lista que será adicionado as Diferenças da entrada

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
	def calculoHorasExtrasDepoisSaidas(self, hrSaida, listaHrSaidas):
		if listaHrSaidas[0] != '00:00:00':  # Se estiver com valor '00:00:00' é por que não tive Horas extras depois das 17:30.
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

		if listaHrSaidas[0] != '00:00:00':  # Se estiver com valor '00:00:00' é por que não tive Horas extras depois das 17:30.
			print('-------------------------------------------------------------------')
			print('|                     Calulando Horas Saídas                       |          ')
			print('-------------------------------------------------------------------|         |')
			print('Total de Horas Pagas que fiz depois das 17:30 até o momento foi de: ', somaSaida[0], ' *** ##ANOTAÇÔES SAÍDAS:  ##***')
			print('-------------------------------------------------------------------|         |')
		return (somaSaida[0])

def calculoHorasExtrasPrimeiroPeriodo(request):
	horariosChegadas = ''
	hrEntrada = ''
	hrChegada = ''

	# if 'edtListaAddChegadas' in request.GET:
	horariosChegadas = request.GET.get('edtListaAddChegadas', "")
	# if request.metho == 'GET':
	# 	# print(':::::::::::::', request.GET.get('edtListaAddChegadas'))
	# 	horariosChegadas = request.GET.get('edtListaAddChegadas')  # string que trago do front com todos os horarios
	# 	#print('Horarios de Chegada-------- : ', horariosChegadas)
	# else:
	# 	horariosChegadas = ''

	listaHrChegadas = horariosChegadas.split(',')  # convertendo em uma lista a string que trouxe do front

	# Referente ao calculo antes de começar a trabalhar
	if 'hrEntrada' in request.GET:
		hrEntrada = request.GET['hrEntrada']
	else:
		hrEntrada = ''
	if 'hrChegada' in request.GET:
		hrChegada = request.GET['hrChegada']
	else:
		hrChegada = ''

	if (hrEntrada != '') and (horariosChegadas != ''):  # and (hrChegada != ''):
		calculoHorasExtrasAntesEntradas = calculo(hrEntrada, hrChegada, listaHrChegadas).calculoHorasExtrasAntesEntradas(hrEntrada, listaHrChegadas)
	else:
		calculoHorasExtrasAntesEntradas = ''

	# return render(request,'calculaHorasDia/calculaHorasDia.html', {'hrEntrada':hrEntrada, 'hrChegada':hrChegada, 'calculoHorasExtrasAntesEntradas':calculoHorasExtrasAntesEntradas})
	return calculoHorasExtrasAntesEntradas


def calculoHorasExtrasSegundoPeriodo(request):

	if 'edtListaAddQueSaiu' in request.GET:
		horariosSaidas = request.GET.get('edtListaAddQueSaiu')  # string que trago do front com todos os horarios
		# print('Horarios de Saida: ', horariosSaidas)
	else:
		horariosSaidas = ''

	listaHrSaidas = horariosSaidas.split(',')
	# print(listaDeHorarios)

	# Referente ao calculo depois que saí do trabalho
	if 'hrSaida' in request.GET:
		hrSaida = request.GET['hrSaida']
	else:
		hrSaida = ''
	if 'hrQueSaiu' in request.GET:
		hrQueSaiu = request.GET['hrQueSaiu']
	else:
		hrQueSaiu = ''

	calculoHorasExtrasDepoisSaidas = ''
	if (hrSaida != '') and (horariosSaidas != ''):
		calculoHorasExtrasDepoisSaidas = calculo(hrSaida, hrQueSaiu, listaHrSaidas).calculoHorasExtrasDepoisSaidas(hrSaida, listaHrSaidas)
	else:
		calculoHorasExtrasDepoisSaidas = ''

	# dic_CalcHrEnt_CalcHrSai = {}
	# if calculoHorasExtrasAntesEntradas != '':
	# 	dic_CalcHrEnt_CalcHrSai['HrExtraEntrada'] = calculoHorasExtrasAntesEntradas
	# if calculoHorasExtrasDepoisSaidas != '':
	# 	dic_CalcHrEnt_CalcHrSai['HrExtraSaida'] = calculoHorasExtrasDepoisSaidas
	# print(dic_CalcHrEnt_CalcHrSai)

	# todo: Estou com o seguinte problema, se mando calcular atraveś do clique do botão , funciona certinho, mas se aperto o F5 , por mais que não tenha nenhum valor dentro dos inputs ele passa pela função e tras sei lá da onde o ultimo valor que adicionei e da um resoltado para o usuário
	# return render(request,'calculaHorasDia/calculaHorasDia.html', {'hrSaida':hrSaida, 'hrQueSaiu':hrQueSaiu, 'calculoHorasExtrasDepoisSaidas':calculoHorasExtrasDepoisSaidas})
	return  calculoHorasExtrasDepoisSaidas

def calculaHorasExtras(request):

	if request.method == 'GET':
		calculoHorasPrimeiroPeriodo = calculoHorasExtrasPrimeiroPeriodo(request)
		print('PRIMEIRO:::: ', calculoHorasPrimeiroPeriodo)

		# calculoHorasSegundoPeriodo = calculoHorasExtrasSegundoPeriodo(request)
		# print('SEGUNDO:::: ',calculoHorasSegundoPeriodo)
		#calculoTotal = calculoHorasPrimeiroPeriodo + calculoHorasSegundoPeriodo

		calculoTotal = calculoHorasPrimeiroPeriodo

		return render(request, 'calculaHorasDia/calculaHorasDia.html', {'calculoHorasPrimeiroPeriodo':calculoHorasPrimeiroPeriodo,
		# 															# 'calculoHorasSegundoPeriodo':calculoHorasSegundoPeriodo,
																'calculoTotal':calculoTotal})

		# return render(request, 'calculaHorasDia/calculaHorasDia.html', {'calculoHorasPrimeiroPeriodo':calculoHorasPrimeiroPeriodo,
		# 															# 'calculoHorasSegundoPeriodo':calculoHorasSegundoPeriodo,
		# 																'calculoTotal':calculoTotal})
	# return render(request, 'calculaHorasDia')
