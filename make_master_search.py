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
    """ join into one big dataframe and then write to master_search """
    os.system("cat 1_search.csv | sed '2 d' > df.csv")
    df_all = pd.read_csv('df.csv')
    for file in glob.glob('*_search.csv'):
        if file == 'master_search.csv':
            break
        elif file != '1_search.csv':
            print(file)
            file2 = 'temp.csv'
            print(file2)
            cmd = "cat {file} | sed '2 d' > {file2}".format(file=file, file2=file2)
            os.system(cmd)
            df_to_add = pd.read_csv(file2, error_bad_lines=False)
            df_all = pd.concat([df_all, df_to_add], axis=0, sort=False)

    df_all.to_csv('master_search.csv')

enter_csvs()
for folder in glob.glob('campaign*'):
    print('going into:', folder)
    if folder != 'campaign_8':
        os.chdir(folder)
        merge_results()
        os.chdir('..')
