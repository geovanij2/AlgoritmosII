# -*- coding: utf-8 -*-
def bazinga(sheldon, raj):
	if (sheldon == raj):
		return 'De novo!'

	if (sheldon == 'tesoura' and raj == 'papel'):
		return 'Bazinga!'
	elif (raj == 'tesoura' and sheldon == 'papel'):
		return 'Raj trapaceou!'

	elif (sheldon == 'papel' and raj == 'pedra'):
		return 'Bazinga!'
	elif (raj == 'papel' and sheldon == 'pedra'):
		return 'Raj trapaceou!'

	elif (sheldon == 'pedra' and raj == 'lagarto'):
		return 'Bazinga!'
	elif (raj == 'pedra' and sheldon == 'lagarto'):
		return 'Raj trapaceou!'

	elif (sheldon == 'lagarto' and raj == 'Spock'):
		return 'Bazinga!'
	elif (raj == 'lagarto' and sheldon == 'Spock'):
		return 'Raj trapaceou!'

	elif (sheldon == 'Spock' and raj == 'tesoura'):
		return 'Bazinga!'
	elif (raj == 'Spock' and sheldon == 'tesoura'):
		return 'Raj trapaceou!'

	elif (sheldon == 'tesoura' and raj == 'lagarto'):
		return 'Bazinga!'
	elif (raj == 'tesoura' and sheldon == 'lagarto'):
		return 'Raj trapaceou!'

	elif (sheldon == 'lagarto' and raj == 'papel'):
		return 'Bazinga!'
	elif (raj == 'lagarto' and sheldon == 'papel'):
		return 'Raj trapaceou!'

	elif (sheldon == 'papel' and raj == 'Spock'):
		return 'Bazinga!'
	elif (raj == 'papel' and sheldon == 'Spock'):
		return 'Raj trapaceou!'

	elif (sheldon == 'Spock' and raj == 'pedra'):
		return 'Bazinga!'
	elif (raj == 'Spock' and sheldon == 'pedra'):
		return 'Raj trapaceou!'

	elif (sheldon == 'pedra' and raj == 'tesoura'):
		return 'Bazinga!'
	elif (raj == 'pedra' and sheldon == 'tesoura'):
		return 'Raj trapaceou!'

t = int(input())
for i in range(1, t+1):
	sheldon, raj = input().split()
	print('Caso #' + str(i) + ': ' + bazinga(sheldon, raj))
