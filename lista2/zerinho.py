# -*- coding: utf-8 -*-

def calcula_jogo(person, play, counter):
	if play == '0':
		counter['0'] = (counter['0'][0]+1, person)
	else:
		counter['1'] = (counter['1'][0]+1, person)

def avalia_jogo(counter):
	if counter['0'][0] == 0:
		return '*'
	elif counter['0'][0] == 1:
		return counter['0'][1]
	elif counter['0'][0] == 2:
		return counter['1'][1]
	else:
		return '*'

while True:
	try:
		counter = {
			'0': (0, ''),
			'1': (0, '')
		}
		jogadores = ['A', 'B', 'C']
		jogadas = input().split()
		for i, jogada in enumerate(jogadas):
			calcula_jogo(jogadores[i], jogada, counter)
		print(avalia_jogo(counter))

	except EOFError:
		break
