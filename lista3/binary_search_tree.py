class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value > self.value:
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)
		else:
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.insert(value)

	def pre_order(self, result):
		result.append(str(self.value))
		if self.left is not None:
			self.left.pre_order(result)
		if self.right is not None:
			self.right.pre_order(result)

	def post_order(self, result):
		if self.left is not None:
			self.left.post_order(result)
		if self.right is not None:
			self.right.post_order(result)
		result.append(str(self.value))

	def in_order(self, result):
		if self.left is not None:
			self.left.in_order(result)
		result.append(str(self.value))
		if self.right is not None:
			self.right.in_order(result)

C = int(input())

for test_case in range(1, C+1):
	N = int(input())
	numbers = [ int(i) for i in input().split() ]

	bst = None

	for i in numbers:
		if bst is None:
			bst = Node(i)
		else:
			bst.insert(i)

	pre_order = []
	in_order = []
	post_order = []

	bst.pre_order(pre_order)
	bst.in_order(in_order)
	bst.post_order(post_order)

	print("Case %d:" % (test_case))
	print("Pre.: %s" % ' '.join(pre_order))
	print("In..: %s" % ' '.join(in_order))
	print("Post: %s" % ' '.join(post_order))
	print()
