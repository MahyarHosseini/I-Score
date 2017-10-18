#import math

#Y is a list of the target values
#y_avg is the global average of target values
#total_num is the total number of input records (X, y) where X is vector of explanatory variable and y is the# dependent/taregt variable

def compute_iscore(Y, Y_cells_avg):
    total_num = len(Y)
    y_sum = 0
    for y in Y:
        y_sum += y
    y_avg = float(y_sum)/len(Y)
        

    num = 0
    for j in range(len(Y_cell_avg)):
        num += pow(len(Y_cell_avg[j]), 2) * pow((Y_cells_avg[j] - y_avg), 2)
    
    denom = 0
    for i in range(total_num):
        denom += pow((Y[i] - y_avg), 2)

    if n == 0:
        print("Error: Denominator is zero!")
        return

    return float(num)/denom
    

