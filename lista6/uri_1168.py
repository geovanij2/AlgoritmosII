num_to_LED = {
	'1': 2,
	'2': 5,
	'3': 5,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 3,
	'8': 7,
	'9': 6,
	'0': 6,

}


N = int(input())

for _ in range(N):

	num = input()

	count = 0

	for char in num:
		count += num_to_LED[char]

	print("%d leds" % count)
