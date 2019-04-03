

N = int(input())

for _ in range(N):
	line = input()
	count_diamonds = 0
	count_open = 0
	for char in line:
		if char == '<':
			count_open += 1
		elif char == '>' and count_open > 0:
			count_open -= 1
			count_diamonds += 1
		else:
			continue
	print(count_diamonds)
