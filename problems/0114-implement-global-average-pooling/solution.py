import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
    # Your code here
    h,w,c = x.shape
    a =np.array([])
    for i in range(c):
        a = np.append(a, x[:,:,i].sum()/(h*w))
    return a