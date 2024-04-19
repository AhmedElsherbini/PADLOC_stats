#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:11:16 2023

@author: ahmed
"""
#########################################
import pandas as pd
import glob
import os
import argparse
import openpyxl
#########################################
my_parser = argparse.ArgumentParser(description='Welcome!')
print("example: $ python pad_loc_stats.py -i ./txt -p Corynebacterium")



my_parser.add_argument('-i','--input_dir',
                       action='store',
                        metavar='input_dir',
                       type=str,
                       help="input_dir")

my_parser.add_argument('-p','--prefix',
                       action='store',
                        metavar='prefix',
                       type=str,
                       help="prefix")


###########################################
# Execute the parse_args() method
args = my_parser.parse_args()

###########################################
path  = args.input_dir

ff = args.prefix
############################################
#path = "/media/ahmed/CC69-620B6/00_Ph.D/DATA_results/0_accolens_prop_database_work/0_analysis/27_padLOC_immunity"

#os.chdir(path)

all_files = glob.glob(os.path.join(path, "*.csv"))

df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

df['freq'] = df.groupby('system')['system'].transform('count')

df1 = df[['system', 'freq']]

df1 = df1.drop_duplicates(subset=['system'])



#plot = df1.plot.pie(y='system', figsize=(7, 7))


#file_name = 'CM.xlsx'


df1['relative_freq'] = df1[['freq']].div(int(len(all_files)), axis=0)

df1 = df1.sort_values('relative_freq', ascending=False)
os.chdir(path)

df1.to_csv("%s_frequency.xlsx"%(ff),index=False,sep=',')

########################################################
#path = "/media/ahmed/CC69-620B6/00_Ph.D/DATA_results/0_accolens_prop_database_work/0_analysis/27_padLOC_immunity"

#os.chdir(path)
file_names = os.listdir()

###########################################

    
data_frames = []

for file_name in file_names:
    if file_name.endswith(".csv"):
        df3 = pd.read_csv(file_name)
        df3 = df3[["system"]]
        df3 = df3.drop_duplicates(subset=['system'])
        df3 = df3.reset_index(drop=True)
        df3 = df3.rename(columns={"system": str(file_name)[:-11]})     
        df3 = df3.T
        data_frames.append(df3)

merged =  pd.concat(data_frames, axis=0)

melted = pd.melt(merged.reset_index(), id_vars='index')
melted = melted.dropna(subset=['value'])
melted = melted.drop(melted.columns[1], axis=1)
melted = melted.sort_values('index')
matrix =  pd.crosstab(melted['index'], melted['value'])
#file_name = 'Matrix.xlsx'

matrix.to_csv("%s_presence_absence.xlsx"%(ff),index=True,sep=',')
