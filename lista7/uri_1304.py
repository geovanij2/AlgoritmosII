distance = 0
time = 0
old_vel = None

while True:
	try:
		line = input()
		if len(line) == 8:
			h, m, s = [int(i) for i in line.split(':')]

			distance += (((h*3600 + m*60 + s) - time) * old_vel)/3600

			print('%02d:%02d:%02d %.2f km' % (h, m, s, distance))
			time = h*3600 + m*60 + s
		else:
			timestamp, vel = line.split()
			h, m, s = [int(i) for i in timestamp.split(':')]
			vel = int(vel)

			if time != 0:
				distance += (((h*3600 + m*60 + s) - time) * old_vel)/3600

			old_vel = vel
			time = h*3600 + m*60 + s
	except EOFError:
		break
