import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n= len(data)
    ind = np.random.default_rng(seed).permutation(n)
    data= data[ind]
    ans = []
    ans.append(data[: int(n*train_frac)])
    ans.append(data[int(n*train_frac) : int(n*train_frac) + int(n*validation_frac)])
    ans.append(data[int(n*train_frac) + int(n*validation_frac):])

    return ans