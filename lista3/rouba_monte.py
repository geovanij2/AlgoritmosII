def isTopOfSomeoneElsePile(score_table, card_of_turn, player_turn):
	for key, value in score_table.items():
		if key != player_turn and value == card_of_turn:
			return True

while True:
	number_of_cards, number_of_players = [ int(i) for i in input().split() ]
	if number_of_cards == number_of_players == 0:
		break

	deck = [ int(i) for i in input().split() ]

	player_turn = 1
	cards_on_table = set()
	score_table = {}
	for i in range(1, number_of_players+1):
		score_table[i] = (None, 0)

	while (len(deck) > 0):
		card_of_turn = deck.pop(0)
		if card_of_turn in cards_on_table:
			cards_on_table.discard(card_of_turn)
			score_table[player_turn] = (card_of_turn, score_table[player_turn][1] + 2)
			continue
		else:
			for key, value in score_table.items():
				if key != player_turn and value[0] == card_of_turn:
					score_table[player_turn] = (card_of_turn, score_table[player_turn][1] + score_table[key][1] + 1)
					score_table[key] = (None, 0)
					break
				elif key == player_turn and value[0] == card_of_turn:
					score_table[player_turn] = (card_of_turn, score_table[player_turn][1] + 1)
					break
			else:
				cards_on_table.add(card_of_turn)
				player_turn = (player_turn % number_of_players) + 1

	winners = []
	for k, v in score_table.items():
		if len(winners) == 0:
			winners.append((k, v[1]))
		else:
			if v[1] > winners[0][1]:
				winners.clear()
				winners.append((k,v[1]))
			elif v[1] == winners[0][1]:
				winners.append((k,v[1]))
			else:
				continue

	winner_score = winners[0][1]
	winners_2 = [ str(i[0]) for i in winners ]

	print("%d %s" % (winner_score, ' '.join(winners_2)))
