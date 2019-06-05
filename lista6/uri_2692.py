def fixText(text, translator):
	ret = ''

	for char in text:
		if translator.get(char) is not None:
			ret += translator[char]
			continue
		ret += char

	return ret


N, M = [ int(i) for i in input().split() ]
translator = {}

for _ in range(N):
	E, S = input().split()
	translator[E] = S
	translator[S] = E

for _ in range(M):
	text = input()

	print(fixText(text, translator))
