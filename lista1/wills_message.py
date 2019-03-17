# -*- coding: utf-8 -*-
output = ''
while True:
	try:
		alphabet = [char for char in input()]
		n = int(input())
		order = input().split()
		for i in order:
			output += alphabet[int(i)-1]
		print(output)
		output = ''
	except EOFError :
		break
