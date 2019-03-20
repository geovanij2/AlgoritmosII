# -*- coding: utf-8 -*-

while (True):
	sentence =  input()
	if sentence == '*': break
	words = sentence.split()
	letter = words[0][0].lower()
	result = 'Y'
	for word in words:
		if letter != word[0].lower():
			result = 'N'
			break
	print(result)
