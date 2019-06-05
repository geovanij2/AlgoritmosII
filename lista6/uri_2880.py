def enigma(cipher, crib):
	tries = len(cipher) - len(crib) + 1
	counter = 0

	for i in range(tries):
		for j in range(len(crib)):
			if crib[j] == cipher[j+i]:
				break
		else:
			counter += 1

	return counter

cipher = input()
crib = input()

print(enigma(cipher, crib))
