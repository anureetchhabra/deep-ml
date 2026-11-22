import numpy as np
def avg_pool_2d(input_matrix: list[list[float]], pool_size: int) -> list[list[float]]:
    input_matrix = np.array(input_matrix)
    h, w = input_matrix.shape
    # print(h,w)
    op = np.zeros((h//pool_size, w//pool_size))
    for i in range(0, h-pool_size+1, pool_size):
        for j in range(0, w - pool_size+1, pool_size):
            op[i//pool_size][j//pool_size] = np.mean(input_matrix[i:i+pool_size, j:j+pool_size])
            # print(i,j)

    # print(input_matrix.shape)
    return op