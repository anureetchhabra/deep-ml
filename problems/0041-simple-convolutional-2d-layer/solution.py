import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
    kernel_height, kernel_width = kernel.shape
    input_height, input_width = input_matrix.shape

    out_h = ((input_height -kernel_height + 2*padding)//stride) + 1
    out_w = ((input_width-kernel_width + 2*padding)//stride) +1
    output_matrix = np.zeros((out_h, out_w))
    input_matrix =  np.pad(input_matrix, pad_width=padding, mode='constant', constant_values=0)
    input_height, input_width = input_matrix.shape

    for i in range(0,input_height - kernel_height + 1,stride):
        for j in range(0,input_width - kernel_width + 1,stride):
        # Extract the current image patch
            # print(input_matrix[i:i+kernel_height, j:j+kernel_width])
            # print(kernel)
            # print(input_matrix[i:i+kernel_height, j:j+kernel_width]@kernel)
            output_matrix[i//stride,j//stride] = np.sum(input_matrix[i:i+kernel_height, j:j+kernel_width]*kernel)

    
    return output_matrix
