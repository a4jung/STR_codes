import pandas as pd
import math

def isstring(value):
    return isinstance(value, str)

def repeat_length(file):
    data = pd.read_csv(file, sep='\t', header=0, index_col = 0)
    row_id_list = [e for e in list(data.index) if not e.startswith('REPID=X')]
    column_id_list = list(data.columns)
    all_read_length = {}
    
    for i in row_id_list:
        rep_id = i
        row_index = row_id_list.index(rep_id)
        if row_index == 0:
            for i in column_id_list:
                all_read_length[i] = [] 
        for i in column_id_list:
            if i=='motif':
                motif = data.iloc[row_index][i].split('=')[1]
                all_read_length[i].append(motif)
            else:
                if not isstring(data.iloc[row_index][i]) and math.isnan(data.iloc[row_index][i]): 
                    all_read_length[i].append('NA')
                else:
                    all_read_length[i].append(len(motif)*int(data.iloc[row_index][i].split('-')[1])) 
    new_data = pd.DataFrame(all_read_length, columns= all_read_length.keys(), index= row_id_list)
    return new_data