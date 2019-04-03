

while True:
	try:
		n = int(input())
		stack = []
		queue = []
		prio_queue = []
		isStack = True
		isQueue = True
		isPrioQueue = True
		for _ in range(n):
			command, number = [ int(i) for i in input().split() ]
			if (command == 1):
				stack.append(number)
				queue.append(number)
				prio_queue.append(number)
			else:
				if (isStack) and (number != stack.pop()):
					isStack = False
				if (isQueue) and (number != queue.pop(0)):
					isQueue = False
				if len(prio_queue) > 0:
					max_value = max(prio_queue)
					prio_queue.remove(max_value)
					if (isPrioQueue) and (number != max_value):
						isPrioQueue = False
				else:
					isPrioQueue = False


		if (isStack and isQueue) or (isStack and isPrioQueue) or (isQueue and isPrioQueue):
			print('not sure')
		elif isStack:
			print('stack')
		elif isQueue:
			print('queue')
		elif isPrioQueue:
			print('priority queue')
		else:
			print('impossible')
	except EOFError:
		break
