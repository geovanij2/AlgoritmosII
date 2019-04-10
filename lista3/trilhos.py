
while True:
	N = int(input())
	if (N == 0):
		break
	while True:
		cart_order = [ int(i) for i in input().split() ]
		if (cart_order == [0]):
			print()
			break
		else:
			carts = [ i for i in reversed(range(1, N+1)) ]
			station_stack = []
			failed = False

			for out_cart in cart_order:
				while True:
					if len(carts) > 0:
						entering_cart = carts.pop()
						if (entering_cart == out_cart):
							break
						elif (entering_cart < out_cart):
							station_stack.append(entering_cart)
						else:
							carts.append(entering_cart)
							station_top_cart = station_stack.pop()
							if (station_top_cart != out_cart):
								failed = True
							break
					else:
						station_top_cart = station_stack.pop()
						if (station_top_cart != out_cart):
							failed = True
						break

			if (failed):
				print('No')
			else:
				print('Yes')
