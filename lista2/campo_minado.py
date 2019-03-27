# -*- coding: utf-8 -*-

N = int(input())
campo = [0] * N

for i in range(N):
	valor_do_campo = int(input())
	if (valor_do_campo == 1):
		if i == 0:
			campo[i] += 1
			campo[i+1] += 1
		elif i == N-1:
			campo[i] += 1
			campo[i-1] += 1
		else:
			campo[i-1] += 1
			campo[i] += 1
			campo[i+1] += 1

for i in campo:
	print(i)
