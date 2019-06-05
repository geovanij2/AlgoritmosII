def mod(num, a):

    # Initialize result
    res = 0

    # One by one process all digits
    # of 'num'
    for i in range(0, len(num)):
        res = (res * 10 + int(num[i])) % a

    return res

def custom_fib (n, memo):
	n = mod(n, 1500)
	return memo[n-1]

memo = []
memo.append(1)
memo.append(1)

for i in range(2, 1501):
	memo.append((memo[i-1] + memo[i-2]) % 1000)

t = int(input())
for i in range(t):
	n = input()
	print("%03d" % custom_fib(n, memo))
