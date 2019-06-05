def numCarrySum(n1, n2):
	total = 0
	carry = 0
	while not (n1 == n2 == 0):
		a = n1 % 10
		b = n2 % 10
		n1 = n1 // 10
		n2 = n2 // 10
		if (a + b + carry >= 10):
			carry = 1
			total += 1
		else:
			carry = 0

	return total

while True:
	a, b = [int(i) for i in input().split() ]

	if a == b == 0:
		break

	c = numCarrySum(a, b)

	if c == 0:
		print('No carry operation.')
	elif c == 1:
		print('1 carry operation.')
	else:
		print('%d carry operations.' % c)
