def interval_sum(a, b):
	n = b - a + 1

	return int(n * (2*a + n-1)/2)

a, b = [ int(i) for i in input().split() ]

print(interval_sum(a, b))
