import pandas as pd
import math

def concordance(file):
    data = pd.read_csv(file, sep='\t', header=0, index_col = 0)
    row_id_list = [e for e in list(data.index) if not e.startswith('REPID=X')]
    column_id_list = list(data.columns)
    Twin_concordance = {}
    
    for i in row_id_list:
        rep_id = i
        row_index = row_id_list.index(rep_id)
        column_index = 0
        while column_index < len(column_id_list):
            column_id_a1 = column_id_list[column_index]
            column_id_a2 = column_id_list[column_index+2]
            column_id_b1 = column_id_a1 + '.1'
            column_id_b2 = column_id_a2 + '.1'
            twin_id = column_id_a1 + '/' + column_id_a2
            if row_index == 0:
                Twin_concordance[twin_id] = [] 
            if column_id_a1 == column_id_a2[:-1]+str(int(column_id_a2[-1])-1) or column_id_a1 == column_id_a2[:-1]+str(int(column_id_a2[-1])+1):
                if math.isnan(data.iloc[row_index][column_id_a1]) or math.isnan(data.iloc[row_index][column_id_a2]) or \
                math.isnan(data.iloc[row_index][column_id_b1]) or math.isnan(data.iloc[row_index][column_id_b2]):
                    Twin_concordance[twin_id].append('NA')
                    column_index +=4
                elif data.iloc[row_index][column_id_a1] == data.iloc[row_index][column_id_a2] and \
                data.iloc[row_index][column_id_b1] == data.iloc[row_index][column_id_b2]:
                    Twin_concordance[twin_id].append('concordant')
                    column_index +=4
                else:
                    Twin_concordance[twin_id].append('discordant')
                    column_index +=4
            else:
                Twin_concordance[twin_id].append('Twin_ID does not match')
                column_index +=4
    new_data = pd.DataFrame(Twin_concordance, columns= Twin_concordance.keys(), index= row_id_list)
    
    concordant = ['concordant']
    NA = ['NA']
    new_data['Percent Concordance'] = list(new_data.isin(concordant).sum(1) / \
                                  (len(Twin_concordance.keys())-new_data.isin(NA).sum(1)))
    export_excel = new_data.to_excel (r'C:\Users\ana\Documents\SUMMER 2019 Sick Kids\filtered.xlsx', index = True, header=True)
    return new_data