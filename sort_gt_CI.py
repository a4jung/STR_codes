import pandas as pd
import math
import numpy
from statistics import mean

def isstring(value):
    return isinstance(value, str)

def sort_CI(file):
### Takes in a csv or text file and returns a disctionary with confidence intervals (CI) sorted as 
### smaller start of CI = allele a
### bigger start of CI = allele b
### ex. original file may contain:          sorted file will contain:
###              allele a = 51 - 58             allele a = 50 - 59
###              allele b = 50 - 59             allele b = 51 - 58 
### returns a dictionary that can be converted into pandas dataframe

    data = pd.read_csv(file, sep='\t', header=0, index_col = 0)
    index=[e for e in list(data.index) if not e.startswith('REPID=X')]
    columns=list(data.columns)
    sorted_CI={}
    for col in columns:
        sorted_CI[col]=[]
    for i in index:
        sorted_CI['motif'].append(data.loc[i]['motif'])
        col_ind=1
        while col_ind<len(columns):
            col_a=columns[col_ind]
            col_b=columns[col_ind+1]
            value_a=data.loc[i][columns[col_ind]]
            value_b=data.loc[i][columns[col_ind+1]]
            if (not isstring(value_a) and math.isnan(value_a)) or (not isstring(value_b) and math.isnan(value_b)) or \
            value_a.split('-')[0]<=value_b.split('-')[0]:
                sorted_CI[columns[col_ind]].append(value_a)
                sorted_CI[columns[col_ind+1]].append(value_b)
                col_ind+=2
            elif value_a.split('-')[0]>value_b.split('-')[0]:
                sorted_CI[columns[col_ind]].append(value_b)
                sorted_CI[columns[col_ind+1]].append(value_a)
                col_ind+=2
    return sorted_CI
    #new_data = pd.DataFrame(sorted_CI, columns= sorted_CI.keys(), index= index)