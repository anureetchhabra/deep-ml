import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	gradient = np.array(gradient, dtype=float)

	mag = np.linalg.norm(gradient)
	if mag==0:
		return  {'magnitude': mag, 'direction': [0] * len(gradient), 'descent_direction': [0] * len(gradient)}
	a = {'magnitude': mag, 'direction':  gradient/mag, 'descent_direction': -gradient/mag}
	return a