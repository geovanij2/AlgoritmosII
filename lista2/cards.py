# -*- coding: utf-8 -*-

cards_str = input().split()
cards = [ int(i) for i in cards_str ]

if (cards[0] < cards[1] and cards[1] < cards[2] and cards[2] < cards[3] and cards[3] < cards[4]):
	print('C')
elif (cards[0] > cards[1] and cards[1] > cards[2] and cards[2] > cards[3] and cards[3] > cards[4]):
	print('D')
else:
	print('N')
