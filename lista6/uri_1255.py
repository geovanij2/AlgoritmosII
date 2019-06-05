def mostFrequentChar(text):
	counter = {}
	text = text.lower()

	for char in text:
		if not char.isalpha():
			continue
		if counter.get(char) is None:
			counter[char] = 1
		else:
			counter[char] += 1

	most_frequent = []
	max = 0

	for key, value in counter.items():
		if (value > max):
			max = value
			most_frequent.clear()
			most_frequent.append(key)
			continue
		if (value == max):
			most_frequent.append(key)
			continue

	most_frequent.sort()

	return ''.join(most_frequent)

N = int(input())

for _ in range(N):

	text = input()

	print(mostFrequentChar(text))
