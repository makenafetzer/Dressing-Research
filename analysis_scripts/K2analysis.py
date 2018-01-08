import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#change the number in campaign_() to desired campaign for analysis
df = pd.read_csv('../csv_files/campaign_8/search_result.csv')

#columns are KepMag, Kmag, Teff, mass, Radius
KepMag = df['KepMag']
Kmag = df['Kmag'].dropna()
Teff = df['Teff'].dropna()
mass = df['mass'].dropna()
Radius = df['Radius'].dropna()

n_bins = 40

#Use matplotlib to create histograms for each column
plt.xlabel('Radius')
plt.grid(True)
plt.hist(Radius, range = [0, 15], bins = n_bins)
plt.show()
