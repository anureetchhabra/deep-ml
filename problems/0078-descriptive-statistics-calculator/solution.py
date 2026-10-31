import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    n = len(data)
    mean = np.sum(data) / n
    data = np.sort(data)
    if n%2==0:
        median= (data[n//2] + data[(n//2) -1]) / 2
        n_25th_percentile = (data[n//4] +data[(n//4) - 1]) / 2 
        n_75th_percentile = (data[(3*n) // 4] + data[((3*n) // 4) - 1 ])/ 2
    else:
        median = data[n//2]
        n_25th_percentile = data[n//4]
        n_75th_percentile = data[(3*n) // 4]
     
    
    vals, counts = np.unique(data, return_counts=True)
    index = np.argmax(counts)
    mode = vals[index]
    variance = np.sum((data - mean)**2) / n
    std = np.sqrt((variance))
    
    return {'mean': mean, 'median': median, 'mode': mode, 'variance': variance,  'standard_deviation': std, "25th_percentile": float(n_25th_percentile), "50th_percentile": median, "75th_percentile": n_75th_percentile, "interquartile_range": n_75th_percentile - n_25th_percentile}
