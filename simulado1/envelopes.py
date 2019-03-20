# -*- coding: utf-8 -*-

import collections

N, K = input().split()
N = int(N)
K = int(K)

rotulos = input().split()
mapa = {}
for i in range(1,K+1):
	mapa[str(i)] = 0
for char in rotulos:
	mapa[char] += 1
print(mapa.get(min(mapa, key=mapa.get)))
