import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	n = len(y_true)
	c = 0
	for i in range(n):
		if (y_pred[i] == 0 and y_true[i] == 0) or   (y_pred[i] == 1 and y_true[i] == 1):
			c+=1

	return c / n 