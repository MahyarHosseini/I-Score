#import math

def get_iscore(Y, y_avg, Y_cell_avg, n, n_cell_j, m1):
    assert len(Y_cell_avg) == len (n_cell_j)
    assert len(Y) == n

    num = 0
    for j in range(m1):
        num += pow(n_cell_j[j], 2) * pow((Y_cell_avg[j] - y_avg), 2)
    
    denom = 0
    for i in range(n):
        denom += pow((Y[i] - y_avg), 2)

    if n == 0:
        print("Error: Denominator is zero!")
        return

    return float(num)/denom
    

