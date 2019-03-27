# -*- coding: utf-8 -*-

N = int(input())

counter = 10

t1 = int(input())

for _ in range(N-1):
	t = int(input())
	counter += min(t-t1, 10)
	t1 = t

print(counter)
