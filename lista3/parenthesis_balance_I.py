

while True:
	try:
		line = input()
		open_parenthesis = 0
		hasPrinted = False
		for char in line:
			if char == '(':
				open_parenthesis += 1
			elif char == ')' and open_parenthesis > 0:
				open_parenthesis -= 1
			elif char == ')' and open_parenthesis <= 0:
				print('incorrect')
				hasPrinted = True
				break
			else:
				continue

		if not hasPrinted:
			if open_parenthesis == 0:
				print('correct')
			else:
				print('incorrect')

	except EOFError :
		break
