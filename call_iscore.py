import iscore as isc
import pandas
import math
import itertools
import numpy
import string

#The values of each column should be between 0 and 1
#def scale_up(in_list, up_value):
    


def read_file(f_addr):
    df = pandas.read_excel(f_addr)
#    columns = df.columns
    return df


##########################Test if df has changed at the end (i.e., columns is not a view only)
def convert_nominal_to_int(df):
    columns = df.columns
    for c in columns:
        temp_list = []
        temp_dict = {}
        count = 1
        if type(df[c].values[0]) == type(u''):
            for val in df[c].values:
                if val not in temp_dict:
                    temp_dict[val] = count
                    count += 1
                temp_list.append(temp_dict[val])
            df[c] = pandas.DataFrame({c: temp_list})
    return df


##########################Test if df has changed at the end (i.e., columns is not a view only)
#Gives us the ganularity of 11
def convert_normalized_to_discrete(df):
    columns = df.columns
    for c in columns:
        temp_list = []
        temp_dict = {}
        if type(df[c].values[0]) == type(numpy.float64(1.4)):#1.4 is just a random number
            for val in df[c].values:
                if val not in temp_dict:
                    temp_dict[val] = int(round(val * 10))
                temp_list.append(temp_dict[val])
            df[c] = pandas.DataFrame({c:temp_list})
    return df


def get_all_initial_seubsets(columns_label_list, subset_len):
    return set(itertools.combinations(columns_label_list, subset_len))    


#Not very efficient in terms of space
def initialize_cells(subset_len, granularity_num):
    cells = [[] for i in range(pow(granularity_num, subset_len))]
    return cells

def correct_name(name):
    #No name starts with number or special character, or has : in the name
    invalidChars = set(string.punctuation)
#    invalidChars = set(string.punctuation.replace("_", ""))
#    if any(char in invalidChars for char in word):
    for char in name:
        if char in invalidChars:
            name = name.replace(char, "_")
    if (name[0] in invalidChars) or name[0].isdigit():
        name = 'dummy' + name
    return name


def partition(df, features_subset, granularity_num):
    cells = initialize_cells(len(features_subset), granularity_num)
#    print 'len(features_subset): ',len(features_subset) 
    cell_inx = 0
    for row_num, row in enumerate(df.itertuples(), 1):
        height = len(features_subset) - 1
        cell_inx = 0
        for f in features_subset:
            cell_inx += getattr(row, f) * pow(granularity_num, height)
            height -= 1
        cells[cell_inx].append(row)
#    print [len(cells[i]) for i in range(len(cells))]
    return cells



#def calculate_avg(column):
#    assert len(column) > 0
#    col_sum = 0
#    for val in column:
#        col_sum += val
#    return col_sum / len(column)



def get_iscore(df, feature_sample, granularity_num, target_feature_name):
    cells = partition(df, feature_sample, granularity_num)
    target_values = df[target_feature_name].values
    cells_avg = []    

    for c in cells:
        temp = 0
        temp_counter = 0
        avg = 0
        for elem in c:
            temp += getattr(elem, target_feature_name)
            temp_counter += 1
        if temp_counter != 0:
            avg = float(temp)/temp_counter
        cells_avg.append(avg)
    
    return isc.compute_iscore(target_values, cells_avg)



#Backward Dropping Algorithm
def BDA(df, initial_features_sample, granularity_num, target_feature_name):
    global_max_iscore = -float('Inf')
    global_max_subset = []
    sample_star = initial_features_sample


    while len(sample_star) > 1: 
        local_max_iscore = -float('Inf')
        local_max_subset = []
        for i in range(len(sample_star)):
            feature_sample = sample_star[:i] + sample_star[i+1:] 
            #Compute I-Score
            iscore = get_iscore(df, feature_sample, granularity_num, target_feature_name)
             
            if iscore > local_max_iscore:
                local_max_iscore = iscore
                local_max_subset = feature_sample

        #Drop a variable
        sample_star = local_max_subset
       
#        print 'local ',local_max_iscore, 'global ', global_max_iscore,  (local_max_iscore > global_max_iscore)
        #Keep the best I-Score
        if local_max_iscore > global_max_iscore:
            global_max_iscore = local_max_iscore
            global_max_subset = local_max_subset
#        print 'global_max_subset', global_max_subset
    return global_max_iscore, global_max_subset
    
     

if __name__ == '__main__':
    f_addr = '/home/seyedmah/Desktop/normalized_data_sep29.xlsx'
    target_feature_name = 'skip_percentage'
    initial_subset_len = 3
    granularity_num = 11#It is fixed according to convert_normalized_to_discrete function
    max_iscore = -float('Inf')
    max_subset = []

    df = read_file(f_addr)   
    #print 'df1: ', df, '\n'
    df = convert_nominal_to_int(df)
    #print 'df2: ', df, '\n'
    df = convert_normalized_to_discrete(df)
    #print 'df3: ', df, '\n\n'

    #Standard columns' name: starts with no number of special characters
    temp = {}
    for name in df.columns:
        temp[name] = correct_name(name) 
    df = df.rename(columns = temp)
    
 
    #Remove target column for creating the feature sets
    df2 = df.copy(deep=True)
######Check is the drop function creats a copy of df2 or use aliasing???
    df2 = df2.drop(target_feature_name, 1)#where 1 is the axis number (0 for rows and 1 for columns)
    all_seubsets = get_all_initial_seubsets(df2.columns, initial_subset_len)


    for s in all_seubsets:
        #Get the feature set with the highest I-Score according to the initial set 
        iscore, selected_set = BDA(df, s, granularity_num, target_feature_name)
        if iscore > max_iscore:
            max_iscore = iscore
            max_subset = selected_set 

    print 'Best I-Score: ', max_iscore
    print 'Best feature set: ', max_subset










