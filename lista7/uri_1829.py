fat = [1]
for i in range(1, 10001):
	fat.append(fat[i-1] * i)

n = int(input())

prints = []
winner = 0

for r in range(1,n+1):
	a, b = [int(i) for i in input().split('^') ]

	lucas = a ** b

	n, _ = [ i for i in input().split('!') ]

	pedro = fat[int(n)]

	if lucas > pedro:
		prints.append('Rodada #%d: Lucas foi o vencedor' % r)
		winner += 1
	else:
		prints.append('Rodada #%d: Pedro foi o vencedor' % r)
		winner -= 1

if winner > 0:
	print('Campeao: Lucas!')
elif winner == 0:
	print('A competicao terminou empatada!')
else:
	print('Campeao: Pedro')

for p in prints:
	print(p)
