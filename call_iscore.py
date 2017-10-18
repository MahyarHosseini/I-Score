import iscore
import pandas
import math
import itertools

#The values of each column should be between 0 and 1
#def scale_up(in_list, up_value):
    


#def scale_up_column(col, up_value):

def read_file(f_addr):
    df = pandas.read_excel(f_addr)
    columns = df.columns
    return df, columns


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


#Gives us the ganularity of 11
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


def get_all_initial_seubsets(columns_label_list, subset_len):
    return set(itertools.combinations(columns_label_list, subset_len))    


#Not very efficient in terms of space
def initialize_cells(subset_len, granularity_num):
    cells = [[] for i in range(pow(granularity_num, subset_len)]
    return cells


#The tree depth is equal with the length of features_subset
def partition(df, features_subset, granularity_num):
    cells = initialize_cells(len(features_subset), granularity_num)
#    depth = 0
    cell_inx = 0
    height = len(features_subset) - 1
    for row_num, row in enumerate(df.itertuples(), 1)
        for f in range(len(features_subset)):
            cell_inx += row[f] * pow(granularity_num, height)
            height -= 1
        cells[cell_inx] = row
    return cells



def calculate_avg(column):
    assert len(column) > 0
    col_sum = 0
    for val in column:
        col_sum += val
    return col_sum / len(column)



def compute_iscore(df, feature_sample, granularity_num, target_feature_name):
    cells = (df, feature_sample, granularity_num)
    target_values = df.columns[target_feature_name].values
    cells_avg = []    

    for c in cells:
        temp = 0
        temp_counter = 0
        avg = 0
        for elem in cells:
            temp += elem[target_feature_name]
            temp_counter += 1
        if temp_counter != 0:
            avg = float(temp)/temp_counter
        cells_avg.append(avg)
    
    return compute_iscore(target_values, cells_avg)



#Backward Dropping Algorithm
def BDA(df, initial_features_sample, granularity_num, target_feature_name)
    global_max_iscore = -float('Inf')
    global_max_subset = []
    sample_start = initial_features_sample

    while len(sample_star > 1) 
        local_max_iscore = -float('Inf')
        local_max_subset = []
        for i in range(sample_star):
            feature_sample = sample_star[:i] + sample_star[i+1:] 
            #Compute I-Score
            iscore = compute_iscore(df, feature_sample, granularity_num, target_feature_name)
    
            if iscore > local_max_iscore:
                local_max_iscore = iscore
                local_max_subset = feature_sample

        #Drop a variable
        sample_star = local_max_subset

        #Keep the best I-Score
        if local_max_iscore > global_max_iscore:
            global_max_iscore = local_max_iscore
            global_max_subset = global_max_subset
        
    
     

    
