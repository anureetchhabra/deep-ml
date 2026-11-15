
from collections import Counter

def confusion_matrix(data):
    # Implement the function here
    tp,fp,tn,fn = 0,0,0,0
    for i in range(len(data)):
        if data[i][0] == 1 and data[i][1] == 1:
            tp+=1
        elif data[i][0] ==0 and data[i][1] == 0:
            tn+=1 
        elif data[i][0]==1 and data[i][1] == 0:
            fn+=1
        elif data[i][0]==0 and data[i][1] == 1:
            fp+=1
    return [[tp,fn], [fp,tn]]
