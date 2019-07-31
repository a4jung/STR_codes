import pandas as pd
import math

def support_read_discordance(discordance, support_reads_table, repeat_length):
    spanning={}
    spanning['number_of_reads']=[]
    spanning['percent_discordance']=[]
    flanking={}
    flanking['number_of_reads']=[]
    flanking['percent_discordance']=[]
    irr={}
    irr['number_of_reads']=[]
    irr['percent_discordance']=[]
    
    index_list=list(discordance.index)
    columns_list=list(discordance.columns[1:-1])
    for i in index_list:
        for cols in columns_list:
            percent = discordance.loc[i]['Percent Discordance']
            if discordance.loc[i][cols]!='NA' and not cols.endswith('.1'):
                if isstring(support_reads.loc[i][cols]) or not math.isnan(support_reads.loc[i][cols]):
                    read = support_reads.loc[i][cols].split('-')
                if repeat_length.loc[i][cols]<=150:
                    spanning['number_of_reads'].append(int(read[0]))
                    spanning['percent_discordance'].append(discordance.loc[i]['Percent Discordance'])
                    flanking['number_of_reads'].append(int(read[2]))
                    flanking['percent_discordance'].append(discordance.loc[i]['Percent Discordance'])
                elif repeat_length.loc[i][cols]>150:
                    flanking['number_of_reads'].append(int(read[2]))
                    flanking['percent_discordance'].append(discordance.loc[i]['Percent Discordance'])
                    irr['number_of_reads'].append(int(read[4]))
                    irr['percent_discordance'].append(discordance.loc[i]['Percent Discordance'])
            elif discordance.loc[i][cols]!='NA' and cols.endswith('.1'):
                if repeat_length.loc[i][cols]<=150:
                    spanning['number_of_reads'].append(int(read[1]))
                    spanning['percent_discordance'].append(discordance.loc[i]['Percent Discordance'])
                    flanking['number_of_reads'].append(int(read[3]))
                    flanking['percent_discordance'].append(discordance.loc[i]['Percent Discordance'])
                elif repeat_length.loc[i][cols]>150:
                    flanking['number_of_reads'].append(int(read[3]))
                    flanking['percent_discordance'].append(discordance.loc[i]['Percent Discordance'])
                    irr['number_of_reads'].append(int(read[5]))
                    irr['percent_discordance'].append(discordance.loc[i]['Percent Discordance'])
    spanning_reads=pd.DataFrame(spanning, columns= spanning.keys())
    flanking_reads=pd.DataFrame(flanking, columns= flanking.keys())
    irr_reads=pd.DataFrame(irr, columns= irr.keys())
        