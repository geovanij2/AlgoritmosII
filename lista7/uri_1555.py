def rafael(x, y):
	return (3 * x) ** 2 + y ** 2

def beto(x, y):
	return 2 * x ** 2 + (5 * y) ** 2

def carlos(x, y):
	return -100 * x + y ** 3

N =  int(input())

for _ in range(N):
	x, y = [int(i) for i in input().split()]

	if rafael(x, y) > beto(x, y) and rafael(x, y) > carlos(x, y):
		print('Rafael ganhou')
	elif beto(x, y) > rafael(x, y) and beto(x, y) > carlos(x, y):
		print('Beto ganhou')
	else:
		print('Carlos ganhou')
