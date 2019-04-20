E = 0.0001

v = [0] * 100000

def custom_sum(arr, n, h):
	count = 0
	for i in range(n):
		if v[i] > h:
			count += i - h
	return count

while True:
	n, a = [ float(i) for i in input().split() ]
	if n == a == 0:
		break
	summ = 0
	for i, elem in enumerate(input().split()):
		v[i] = int(elem)
		summ += v[i]

	if (summ == a):
		print(':D')
		continue
	if (summ < a):
		print('-.-')
		continue

	upperbound = max(v)
	lowerbound = 0
	while lowerbound <= upperbound:
		guess = (lowerbound + upperbound) / 2
		csum = custom_sum(v, int(n), guess)
		if abs(csum - a) < E:
			print('%0.4f' % guess)
			break
		elif csum > a:
			lowerbound = guess
		else:
			upperbound = guess
