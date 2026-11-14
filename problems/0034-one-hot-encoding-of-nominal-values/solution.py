import numpy as np

def to_categorical(x, n_col=None):
    # Your code here
    n = max(x) + 1
    if n_col!=None:
        onehot = np.zeros((len(x),n_col))
    else:
        onehot = np.zeros((len(x),n))

    for i in range(len(x)):
        onehot[i][x[i]] =1
    return onehot