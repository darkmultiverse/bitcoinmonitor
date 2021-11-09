'''
Monitor de Ocilação de BitCoin V0.6
Autor: Dark Multiverse.
https://economia.awesomeapi.com.br/json/all
'''
#libs
import requests, time, json, datetime
import pygame.mixer, pygame.time
import os 
import pyttsx3

#musica
pygame.mixer.init()
music = pygame.mixer.music

#Pular Espaço
print ("")
print ("Monitor de Ocilação de BitCoin Versão 0.6")
print ("Autor: Dark Multiverse.")
print ("")
a = ("\n_____________________________________________________________________\n")
cls = lambda: os.system('cls')

#valor bitcoin
def obter_valor():
    try:
        requisicao = requests.get('https://economia.awesomeapi.com.br/json/all')
        cotacao = json.loads(requisicao.text)
        today = datetime.datetime.now()
        valor = (float(cotacao['BTC']['bid']))
        return valor
    except:
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