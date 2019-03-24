# -*- coding: utf-8 -*-

from functools import cmp_to_key

def sort_rank(a, b):
	country_a, gold_a, silver_a, bronze_a = a.split()
	country_b, gold_b, silver_b, bronze_b = b.split()
	gold_a = int(gold_a)
	gold_b = int(gold_b)
	silver_a = int(silver_a)
	silver_b = int(silver_b)
	bronze_a = int(bronze_a)
	bronze_b = int(bronze_b)
	if (gold_a > gold_b):
		return 1
	elif (gold_b > gold_a):
		return -1
	else:
		if (silver_a > silver_b):
			return 1
		elif (silver_b > silver_a):
			return -1
		else:
			if (bronze_a > bronze_b):
				return 1
			elif (bronze_b > bronze_a):
				return -1
			else:
				if (country_a > country_b):
					return -1
				elif (country_b > country_a):
					return 1
				else:
					return 0

cmp_items_py3 = cmp_to_key(sort_rank)

N = int(input())
rank = []
for _ in range(N):
	line = input()
	rank.append(line)
rank.sort(key=cmp_items_py3, reverse=True)
for i in rank:
	print(i)
