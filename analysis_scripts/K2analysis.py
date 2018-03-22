import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb
import astropy.units as u
import glob
import make_graph as m

'''
For my first plots:

#change the number in campaign_() to desired campaign for analysis
df = pd.read_csv('../csv_files/campaign_14/search_result.csv')

#columns are KepMag, Kmag, Teff, mass, Radius
KepMag = df['KepMag']
Kmag = df['Kmag'].dropna()
Teff = df['Teff'].dropna()
mass = df['mass'].dropna()
Radius = df['Radius'].dropna()

n_bins = 40

#Use matplotlib to create histograms for each column
#plt.xlabel('Radius')
#plt.grid(True)
#plt.hist(Radius, range = [0, 15], bins = n_bins)
#plt.show()
'''

campaign_str = 'campaign_14'

#For each big proposal in the campaign, create a df so a color-magnitude plot
#can be made for each big df_big_proposal

big_prop_list = glob.glob('../csv_files/%s/big_targets/*' %campaign_str)
temp = [x[-9:-4] for x in big_prop_list]
props_num = []
for i in range(len(temp)):
    try:
        int(temp[i][0])
        props_num.append(temp[i])
    except:
        pass

for proposal in props_num:
    #m.make_logg_CM(campaign_str, int(proposal), 'logg_colored')
    m.make_temp_CM(campaign_str, int(proposal), 'Teff_colored')
