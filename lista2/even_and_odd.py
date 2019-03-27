# -*- coding: utf-8 -*-

N = int(input())
even = []
odd = []
for _ in range(N):
	elem = int(input())
	if (elem % 2 == 0):
		even.append(elem)
	else:
		odd.append(elem)
even.sort()
odd.sort(reverse=True)

for i in even:
	print(i)
for i in odd:
	print(i)
