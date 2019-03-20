# -*- coding: utf-8 -*-
N = int(input())
for i in range(N):
	str_set = input().split()
	str_set.sort(key=len, reverse=True)
	print(' '.join(str_set))
