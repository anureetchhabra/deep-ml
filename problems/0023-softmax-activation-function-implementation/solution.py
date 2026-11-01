import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    sum = 0
    max_score = max(scores)
    import numpy as np 
    for i in range(len(scores)):
        sum += np.exp(scores[i] - max_score)
    for i in range(len(scores)):
        scores[i] = np.exp(scores[i] - max_score) / sum

    return scores