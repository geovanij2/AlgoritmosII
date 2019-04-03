

N = int(input())

for test_case in range(N):
	number_of_base_addresses, number_of_keys = [ int(i) for i in input().split() ]
	keys = [ int(i) for i in input().split() ]
	hash_table = dict()

	for i in range(number_of_base_addresses):
		hash_table[i] = []

	for key in keys:
		hash_table[key%number_of_base_addresses].append(key)

	for k, v in hash_table.items():
		v = [ str(i) for i in v ]
		v.append("\\")
		print("%d -> %s" % (k, ' -> '.join(v)))

	if test_case != N-1:
		print()
