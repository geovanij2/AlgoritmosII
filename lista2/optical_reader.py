# -*- coding: utf-8 -*-

helper = {
	0: 'A',
	1: 'B',
	2: 'C',
	3: 'D',
	4: 'E',
}


while True:
	N = int(input())
	if N == 0:
		break

	for _ in range(N):
		alternatives = [ int(i) for i in input().split() ]
		candidates = [ i for i, scan_value in enumerate(alternatives) if scan_value <= 127 ]
		if (len(candidates) == 1):
			print(helper[candidates[0]])
		else:
			print('*')
