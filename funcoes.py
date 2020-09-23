import init, requests, time
from datetime import date

#funcao para criar a mensagem
def report(dados):
	#request do chamados
	URL = 'https://api.tomticket.com/chamados/' + init.tt_key + '/1?situacao=0,1,2,3&departament_id=' + dados['dp_id']
	page = requests.get(URL)

	#cria o json dos chamados
	lista = page.json()

	#cria os objetos de tempo
	hoje = date.today()
	t = time.localtime()
	hora = time.strftime("%H:%M", t)

	#cria a mensagem
	mensagem = "\033⚠️ TOMTICKET — " + dados['dp_name'] + "\n" + str(hoje.day).zfill(2) + " de " + mes(hoje.month) + " às " + str(hora) + "\n\n——————————————\n"
	mensagem += "Aguardando Interação:\n\n"

	for item in lista['data']:
		if item['ultimasituacao'] == 0 or item['ultimasituacao'] == 1:
			mensagem += sla(item['sla_deadline_cumprido']) + " #" + str(item['protocolo']) + " | " + item['titulo'] + " | " + item['atendente'] + "\n"

	mensagem += "\n——————————————\nEm Processo:\n\n"

	for item in lista['data']:
		if item['ultimasituacao'] == 2 or item['ultimasituacao'] == 3:
			mensagem += sla(item['sla_deadline_cumprido']) + " #" + str(item['protocolo']) + " | " + item['titulo'] + " | " + item['atendente'] + "\n"

	mensagem += "\n——————————————\n\n" + str(sla_count(lista)) + " chamados expirados de " + str(lista['total_itens']) + " no total."

	return mensagem


#nome do mês
def mes(arg):
	if arg == 1:
		return "janeiro"
	if arg == 2:
		return "fevereiro"
	if arg == 3:
		return "março"
	if arg == 4:
		return "abril"
	if arg == 5:
		return "maio"
	if arg == 6:
		return "junho"
	if arg == 7:
		return "julho"
	if arg == 8:
		return "agosto"
	if arg == 9:
		return "setembro"
	if arg == 10:
		return "outubro"
	if arg == 11:
		return "novembro"
	if arg == 12:
		return "dezembro"

#define o sla
def sla(arg):
	if arg:
		return "🟢"
	else:
		return "🔴"

#contagem de chamados
def sla_count(jsonobj):
	est = 0;
	for ticket in jsonobj['data']:
		if ticket['sla_deadline_cumprido']:
			pass
		else:
			est += 1
	return est