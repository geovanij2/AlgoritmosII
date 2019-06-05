
def fair_coin_flipping(n1, n2):
	return n1 / (n1 + n2)

def unfair_coin_flipping(n1, n2, p, q):
	return (1-(q/p)**n1)/(1-(q/p)**(n1+n2))


while True:
	ev1, ev2, at, d = [ int(i) for i in input().split() ]

	if ev1 == ev2 == at == d == 0:
		break

	n1, n2 = 0, 0

	while(ev1 > 0):
		ev1 -= d
		n1 += 1

	while(ev2 > 0):
		ev2 -= d
		n2 += 1

	if at == 3:
		print('%.1f' % (fair_coin_flipping(n1, n2) * 100))
	else:
		print('%.1f' % (unfair_coin_flipping(n1, n2, at/6, 1-(at/6)) * 100))
