# -*- coding: utf-8 -*-
def percentage(value, total):
	return (value/total)*100

n = int(input())
c = r = s = total = 0
for i in range(n):
	amount, animal = input().split()
	amount = int(amount)
	total += amount
	if animal == 'C':
		c += amount
	elif animal == 'R':
		r += amount
	else:
		s += amount

print('Total: %d cobaias' % total)
print('Total de coelhos: %d' % c)
print('Total de ratos: %d' % r)
print('Total de sapos: %d' % s)
print('Percentual de coelhos: %0.2f' % percentage(c, total) + ' %')
print('Percentual de ratos: %0.2f' % percentage(r, total) + ' %')
print('Percentual de sapos: %0.2f' % percentage(s, total) + ' %')
