# -*- coding: utf-8 -*-
def foo(a1, a2, a3):
	a1_time = (a2 * 2) + (a3 * 4)
	a2_time = (a1 * 2) + (a3 * 2)
	a3_time = (a1 * 4) + (a2 * 2)
	return min(a1_time, a2_time, a3_time)

a1 = int(input())
a2 = int(input())
a3 = int(input())

print(foo(a1,a2,a3))
