"""
Takes the search outputs from MAST and makes one big master search file with
just one row for headers
"""

import os
import glob
import csv
import subprocess
import pandas as pd

def enter_csvs():
    os.chdir("csv_files/")

def merge_results():
    df = pd.read_csv('1_search.csv')
    for file in glob.glob('*_search.csv'):
        if file == 'master_search.csv':
            break
        elif file == '1_search.csv':
            cmd = "cat {file} | sed '2 d' > master_search.csv".format(file=file)
        else:
            df_to_add = pd.read_csv(file, error_bad_lines=False)
            cols_to_remove = df.columns.difference(df_to_add.columns)
            print('diff columns', cols_to_remove)
            print(file)
            if len(df_to_add.columns) > len(df.columns):
                df_to_add.drop(columns=cols_to_remove)
                df_to_add.to_csv(file)
            elif len(df.columns) > len(df_to_add.columns):
                df.drop(columns=cols_to_remove)
                df.to_csv('1_search.csv')
            cmd = "cat {file} | sed '1,2 d' >> master_search.csv".format(file=file)
        os.system(cmd)

enter_csvs()
for folder in glob.glob('campaign*'):
    print('going into:', folder)
    os.chdir(folder)
    merge_results()
    os.chdir('..')
