while True:
	a, b, c, d = [ int(i) for i in input().split() ]

	if a == b == c == d == 0:
		break

	x = (((a/2)+b)*c)/d

	print('%.5f' % x)
