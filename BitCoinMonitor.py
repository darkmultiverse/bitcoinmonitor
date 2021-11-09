'''
Monitor de Ocilação de BitCoin V0.4
Autor: Dark Multiverse.
http://api.coindesk.com/v1/bpi/currentprice.json
https://www.melhorcambio.com/dolar-hoje
'''
#libs
import urllib.request, json, time    
import pygame.mixer, pygame.time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os 

#musica
pygame.mixer.init()
music = pygame.mixer.music

#Pular Espaço
print ("")
print ("Monitor de Ocilação de BitCoin Versão 0.4")
print ("Autor: Dark Multiverse.")
print ("")
a = ("\n_____________________________________________________________________\n")
cls = lambda: os.system('cls')

#Calculo do Valor do Dólar Através da API
req = Request('https://www.melhorcambio.com/dolar-hoje', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

lista_valores = []

for valor in soup.findAll('td', class_='tdvalor'):
    lista_valores.append(valor.text)

dolar = lista_valores[2].split('R$')
dolar = float(dolar[1].replace(',', '.'))

# Obter Valor Atual do Bitcoin em Dólar
def obter_valor():
	try:
		url = "http://api.coindesk.com/v1/bpi/currentprice.json"
		with urllib.request.urlopen(url) as url:
			response = url.read()
			data = json.loads(response.decode('utf-8'))
			valor = float(data['bpi']['USD']['rate'].replace(",", ""))
			return valor*dolar 
	except urllib.error.HTTPError:
		print("URL inexistente!")

#loop de calculo do bitcoin
def exibir_valores(tempo=1):
	valor = obter_valor()
	nova_cotacao = True
	print("1 Bitcoin atualmente vale %.2f Reais!" % valor + a)
	while True:
		valor_atual = obter_valor()
		if valor_atual < valor:
			print("---> Preço do Bitcoin descendo: 1 Bitcoin vale %.2f Reais!" % valor_atual + a), music.load('quebra.mp3'), music.play()
			nova_cotacao = True
		elif valor_atual > valor:
			print("---> Preço do Bitcoin subindo: 1 Bitcoin vale %.2f Reais!" % valor_atual + a), music.load('dinheiro.mp3'), music.play()
			nova_cotacao = True
		else:
			if nova_cotacao == True:
				print("Aguardando uma nova cotação..." + a)
				nova_cotacao = False
		valor = valor_atual
		time.sleep(tempo)
    
exibir_valores()