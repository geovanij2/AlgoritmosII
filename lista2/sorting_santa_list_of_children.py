# -*- coding: utf-8 -*-

N = int(input())

behaved_counter = 0
children = []
for _ in range(N):
	behaved, name = input().split()
	if behaved == '+':
		behaved_counter += 1
	children.append(name)
if (len(children) > 0):
	children.sort()
	print('\n'.join(children))
print('Se comportaram: %d | Nao se comportaram: %d' % (behaved_counter, N - behaved_counter))
