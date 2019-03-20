# -*- coding: utf-8 -*-
def create_dict(line):
	return {
		'A': set([line[0], line[1]]),
		'B': set([line[2], line[3]]),
		'C': set([line[4], line[5]]),
		'D': set([line[6], line[7]]),
		'E': set([line[8], line[9]])
	}

count = 1
while True:
	N = int(input())
	if(N == 0): break
	passwords = []
	for _ in range(N):
		line = input().split()
		passwords.append((create_dict(line), line[10::]))

	for i in range(len(passwords)):
		if i == 0:
			password = [ passwords[i][0][char] for char in passwords[i][1] ]
		else:
			for j, char in enumerate(passwords[i][1]):
				if (len(password[j]) > 1):
					password[j] = password[j] & passwords[i][0][char]

	print('Teste ' + str(count))
	password = [ i.pop() for i in password ]
	print(' '.join(password) + ' \n')
	count += 1
