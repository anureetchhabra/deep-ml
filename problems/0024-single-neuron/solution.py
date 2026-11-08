import math
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	# Your code here
	features = np.array(features)
	labels = np.array(labels)
	weights = np.array(weights)

	z = features@weights + bias
	probabilities = sigmoid(z)
	mse = np.sum((probabilities - labels)**2) / len(labels)
	return probabilities, mse