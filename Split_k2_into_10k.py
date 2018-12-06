"""
Splits IDs into files with at most 10k rows to fit with the MAST data retrieval system
"""
import os
import glob
import csv
import subprocess

def enter_csvs():
    os.chdir("csv_files/")

def extract_epic_ids(num):
    """
    Returns number of IDs
    """
    cmd = "cat K2Campaign{num}targets.csv | cut -d , -f 1 | sed '1 d' > EpicIDs.csv".format(num=num)
    os.system(cmd)
    output = subprocess.check_output(['wc', '-l', 'EpicIDs.csv'])
    output = output.decode()
    entries_num = output[3:8]
    entries_num.replace(" ", "")
    return int(entries_num)

def split_ids(num_rows):
    """
    Splits the epic IDs into files with 10k lines
    """
    if num_rows < 10000:
        cmd = "cat EpicIDs.csv > 10k_ids.csv"
        os.system(cmd)
    else:
        num_sets = num_rows//10000 + 1
        #number of sets of 10k
        count = 0
        for i in range(1, num_sets + 1):
            new_filename = str(i) + "0k_ids.csv"
            if count == 0:
                beginning = 1
            elif count > 0:
                beginning = (count * 10000) + 1
            ending = i * 10000
            cmd = "sed -n '{beginning},{ending} p' EpicIDs.csv > {file}".format(beginning=str(beginning), ending=str(ending), file=new_filename)
            count += 1
            os.system(cmd)

def make_EpicID_lists():
    """
    Makes the file of complete epic IDs from the campaign to then be split into
    groups of 10k to fit in the MAST search portal
    """
    enter_csvs()
    for folder in glob.glob('campaign*'):
        print('going into:', folder)
        campaign_num = folder[9:]
        if campaign_num != '14':
            os.chdir(folder)
            num_rows = extract_epic_ids(campaign_num)
            split_ids(num_rows)
            os.chdir('..')


make_EpicID_lists()
