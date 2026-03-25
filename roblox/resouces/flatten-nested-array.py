class NestedArray:
	def __init__(self, is_nested, arr):
		self.arr = arr
		self.is_nested = is_nested

# [[1, 2, [3], 4], 5, [6, 7]]
nested_arr = NestedArray(
	True,
	[
		NestedArray(True, [NestedArray(False, 1), NestedArray(False, 2), NestedArray(True, [NestedArray(False, 3)]), NestedArray(False, 4)]),
		NestedArray(False, 5),
		NestedArray(True, [NestedArray(False, 6), NestedArray(False, 7)])
	]
)

class NestedArrayTuple:
	def __init__(self, nested_array, depth):
		self.nested_array = nested_array
		self.depth = depth


def unnest_array(nested_array, depth):
	if not depth or not nested_array.is_nested:
		return nested_array
	stack = []
	res = []
	for array in reversed(nested_array, depth):
		stack.append(NestedArrayTuple(array, depth - 1))
	while stack:
		top = stack.pop()
		if top.depth > 0 and top.nested_array.is_nested:
			stack.append(NestedArrayTuple(array, top.depth - 1))
		else:
			res.append(top.nested_array.arr)
        