# -*- coding: utf-8 -*-
while True:
	N = int(input())
	if N == 0: break
	mary = john = 0
	games = input()
	for char in games:
		if char == '0':
			mary += 1
		elif char == '1':
			john += 1
		else:
			continue
	print('Mary won %d times and John won %d times' % (mary, john))
