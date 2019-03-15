# -*- coding: utf-8 -*-
while True:
	x1, y1, x2, y2 = input().split()
	x1 = int(x1)
	y1 = int(y1)
	x2 = int(x2)
	y2 = int(y2)

	if x1 == y1 == x2 == y2 == 0: break
	elif x1 == x2 and y1 == y2: print(0)
	elif (x1 == x2) or (y1 == y2) or (abs(x2-x1) == abs(y2-y1)):
		print(1)
	else:
		print(2)
