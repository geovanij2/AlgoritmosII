def dietPlan(diet, breakfast, lunch):

	concat = breakfast + lunch

	for char in concat:
		if char not in diet:
			return 'CHEATER'

	ret = []

	for char in diet:
		if char not in concat:
			ret.append(char)

	ret.sort()

	return ''.join(ret)



N = int(input())

for _ in range(N):

	diet = input()
	breakfast = input()
	lunch = input()

	print(dietPlan(diet, breakfast, lunch))
