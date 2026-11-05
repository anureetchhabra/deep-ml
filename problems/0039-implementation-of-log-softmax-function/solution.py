import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	scores = np.array(scores)
	sm = []
	sumd = np.sum(np.exp(scores))
	sm = np.log(np.exp(scores)/ sumd)
	return sm