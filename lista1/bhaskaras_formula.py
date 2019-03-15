# -*- coding: utf-8 -*-
import math

def bhaskara(a, b, c):
	if (a == 0): raise Exception('Impossivel calcular')
	delta = b**2 + (-4*a*c)
	if (delta < 0): raise Exception('Impossivel calcular')
	sqrt_delta = math.sqrt(delta)
	x1 = (-b + sqrt_delta) / (2*a)
	x2 = (-b - sqrt_delta) / (2*a)
	return x1, x2


a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

try:
	r1, r2 = bhaskara(a, b, c)
	print('R1 = %0.5f' % r1)
	print('R2 = %0.5f' % r2)
except:
	print('Impossivel calcular')
