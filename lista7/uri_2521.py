import math


while True:
	try:
		r, la, lo = [ int(i) for i in input().split() ]

		la, lo = math.radians(la), math.radians(lo)

		x = round(math.sin(lo) * math.cos(la) * r, 2) + 0
		y = round(math.sin(la) * r, 2) + 0
		z = round(-math.cos(lo) * math.cos(la) * r, 2) + 0

		print('%.2f %.2f %.2f' % (x, y, z))
	except EOFError:
		break
