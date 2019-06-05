fat = [1]
for i in range(1, 4001):
	fat.append(fat[i-1] * i)

def permutations_with_repetition(n, a):
	return fat[n]//fat[a]

t = int(input())

for _ in range(t):
	n, m = [ int(i) for i in input().split() ]

	empty_chairs = n - (2 * m)
	slots = m + empty_chairs

	p = permutations_with_repetition(slots, empty_chairs)

	print((p * (2**m)) % 1300031)
