import iscore
import pandas
#import math


#The values of each column should be between 0 and 1
#def scale_up(in_list, up_value):
    


#def scale_up_column(col, up_value):

def read_file(f_addr):
    df = pandas.read_excel(f_addr)
    columns = df.columns
    return columns

def convert_nominal_to_int(columns):
    for c in columns:
        temp_list = []
        temp_dict = {}
        count = 1
        if type(columns[c].values[0]) == type(''):
            for val in columns[c].values:
                if val not in temp_dict:
                    temp_dict[val] = count
                    count += 1
                temp_list.append(temp_dict[val])
        columns[c] = temp_list
    return columns



def convert_normalized_to_discrete(columns)
    for c in columns:
        temp_list = []
        temp_dict = {}
        if type(columns[c].values[0]) == float:
            for val in columns[c].values:
                if val not in temp_dict:
                    temp_dict[val] = round(val * 10)
                temp_list.append(temp_dict[val])
        columns[c] = temp_list
    return columns


def calculate_avg(column):
    assert len(column) > 0
    col_sum = 0
    for val in column:
        col_sum += val
    return col_sum / len(column)



#def compute_iscores(columns_data, Y, y_avg, Y_cell_avg, n, n_j, m1):
#    iscore_dict = {}
#    for c in columns_data:
#        
#        col_data = columns_data[c]
#        iscore = get_iscore(col_data, y_avg, Y_cell_avg, n, n_j, m1)

