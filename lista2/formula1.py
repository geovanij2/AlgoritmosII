# -*- coding: utf-8 -*-

while True:
	G, P = input().split()
	G, P = int(G), int(P)
	if (G == 0 and P == 0):
		break
	scores = {}
	for i in range(1, P+1):
		scores[i] = 0

	gps = []
	for i in range(G):
		gps.append([ int(_) for _ in input().split() ])

	S = int(input())
	for _ in range(S):
		s = [ int(_) for _ in input().split() ]
		for gp in gps:
			for pilot, position in enumerate(gp):
				pilot += 1
				if position <= s[0]:
					scores[pilot] += s[position]
		winner = max(scores, key=scores.get)
		winners = [ str(i) for i in scores.keys() if scores[i] == scores[winner]]
		print(' '.join(winners))
		for i in range(1, P+1):
			scores[i] = 0
