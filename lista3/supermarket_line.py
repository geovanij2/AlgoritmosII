from queue import PriorityQueue

n, m = [ int(i) for i in input().split() ]
v = [ int(i) for i in input().split() ]
c = [ int(i) for i in input().split() ]
fila = PriorityQueue()
ans = 0

for i in range(n):
	fila.put((0,i))

for elem in c:
	l, id = fila.get()
	fila.put((l+v[id]*elem, id))
	ans = max(ans, l+v[id]*elem)

print(ans)
