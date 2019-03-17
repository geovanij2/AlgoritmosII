# -*- coding: utf-8 -*-
def parseInput(str):
	if (str == '--*'):
		return 1
	elif (str == '-*-'):
		return 2
	elif (str == '-**'):
		return 3
	elif (str == '*--'):
		return 4
	elif (str == '*-*'):
		return 5
	elif (str == '**-'):
		return 6
	elif (str == '***'):
		return 7
	else:
		return 0

s = 0
while True:
	try:
		bla = input()
		if (bla == 'caw caw'):
			print(s)
			s = 0
		else:
			s += parseInput(bla)
	except EOFError :
		break
