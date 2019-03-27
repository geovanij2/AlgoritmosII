# -*- coding: utf-8 -*-

from functools import cmp_to_key

def c_modulo(num, mod):
	if num < 0:
		return -(abs(num) % mod)
	else:
		return num % mod

def isEven(num):
	return num % 2 == 0

def custom_sort(a, b):
	value_a = c_modulo(a, M)
	value_b = c_modulo(b, M)

	if value_a > value_b:
		return -1
	elif value_b > value_a:
		return 1
	else:
		if not isEven(a) and isEven(b):
			return 1
		elif isEven(a) and not isEven(b):
			return -1
		elif not isEven(a) and not isEven(b):
			if a > b: return 1
			elif b > a: return -1
			else: return 0
		else:
			if a > b: return -1
			elif b > a: return 1
			else: return 0


cmp_items_py3 = cmp_to_key(custom_sort)

while True:
	N, M = [ int(i) for i in input().split() ]
	array = []
	if (N == 0 and M == 0):
		print('0 0')
		break
	for _ in range(N):
		array.append(int(input()))
	array.sort(key=cmp_items_py3, reverse=True)
	print('%d %d' % (N, M))
	for i in array:
		print(i)
