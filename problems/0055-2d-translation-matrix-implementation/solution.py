import numpy as np
def translate_object(points, tx, ty):
    points = np.array(points)
    t = np.array([tx,ty])

    for i in range(len(points)):
        points[i]+=t
    # print(points)
    return points
