import numpy as np

def make_diagonal(x):
	# Your code here
	n = len(x)
	a = np.zeros((n, n))
	for i in range(n):
		a[i,i] = x[i]
	return a