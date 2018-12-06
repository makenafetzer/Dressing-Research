"""
This file takes the Unix commands of taking proposals with the format GO#### and
transforming them into epicIDs so that they can easily be input into the MAST
Archive to retreive data collected by the K2 Campaign
"""
import os
import glob

def enter_csvs():
    os.chdir("csv_files/")

def big_targets_changer():
    os.chdir("big_targets/")
    for target in glob.glob('GO*'):
        prop_num = target[2:-12]
        print('prop_num', prop_num)
        str = "Cut -d , -f 1 GO{prop}-targets.csv > prop_{prop}.csv".format(prop=prop_num)
        print(target, str)
        print('------')
        os.system(str)
    os.chdir("..")
    #then go back out of big targets

enter_csvs()
for folder in glob.glob('campaign*'):
    print('going into:', folder)
    os.chdir(folder)
    big_targets_changer()
    os.chdir('..')
