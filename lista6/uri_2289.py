while True:
	x, y = [int(i) for i in input().split()]

	if x == y == 0:
		break

	counter = 0

	for char in bin(x ^ y):
		if char == '1':
			counter += 1

	print(counter)
