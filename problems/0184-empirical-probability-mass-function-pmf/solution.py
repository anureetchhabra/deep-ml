import numpy as np
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    values, count = np.unique(samples, return_counts=True)
    # print(values, count)
    n = len(samples)
    ans =[]
    for i in range(len(values)):
        ans.append((values[i], count[i]/n))
    return ans