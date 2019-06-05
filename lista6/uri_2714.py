def getProvisionalPassword(academicRecord):
	if (len(academicRecord) != 20):
		return 'INVALID DATA'
	if (academicRecord[:2] != 'RA'):
		return 'INVALID DATA'
	pswd = ''
	leadingZeros = True

	for char in academicRecord[2:]:
		if leadingZeros and char == '0':
			continue
		if leadingZeros and char != '0':
			leadingZeros = False
			pswd += char
			continue
		if not leadingZeros:
			pswd += char

	return pswd



N = int(input())

for _ in range(N):

	academicRecord = input()

	print(getProvisionalPassword(academicRecord))
