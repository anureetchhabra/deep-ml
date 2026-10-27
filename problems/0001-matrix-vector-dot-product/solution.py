def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	import numpy as np
	r_a, c_a = len(a), len(a[0])
	lb = len(b)
	if c_a != lb:
		return -1
	ans = []
	for i in range(r_a):
		d = np.dot(a[i], b)
		ans.append(d)
	return ans
