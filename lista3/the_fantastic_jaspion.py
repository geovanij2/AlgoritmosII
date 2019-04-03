
T = int(input())

for _ in range(T):
	words_in_dict, lines_in_song = [ int(i) for i in input().split() ]
	translate = dict()
	for _ in range(words_in_dict):
		japonese = input()
		portuguese = input()
		translate[japonese] = portuguese
	for _ in range(lines_in_song):
		line = input().split()
		for i in range(len(line)):
			if translate.get(line[i]):
				line[i] = translate.get(line[i])
		print(' '.join(line))
	print()
