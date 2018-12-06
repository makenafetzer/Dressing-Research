import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdb
import astropy.units as u
import glob

def make_logg_CM(campaign, proposal, folder):
    """
    proposal should be entered as an int
    campaign and folder are strings
    """
    df_all = pd.read_csv('csv_files/%s/master_search.csv' %campaign, low_memory=False)

    df_big_proposal = pd.read_csv('csv_files/%s/big_targets/prop_%d.csv' %(campaign, proposal), low_memory=False)
#Would want the above line to cycle through big_targets

    prop_id = df_big_proposal['EPIC ID']

    df_all = df_all.merge(df_big_proposal, left_on='EPIC', right_on='EPIC ID', how='inner')

    ww = np.where(df_all['Object type'] == 'STAR')
    df_all = df_all.iloc[ww]

    #initializing the data frame for calculating reduced proper motion
    df_pm = pd.DataFrame(columns=['Jmag','Hmag','KepMag','pmra','pmdec',
    'pm','j_min_h','H', 'logg'])

    df_pm['Jmag'] = df_all['Jmag']
    df_pm['Hmag'] = df_all['Hmag']
    df_pm['logg'] = df_all['logg']

    #Removing any row that doesn't have a Jmag and Hmag value
    df_pm = df_pm.dropna(axis=0, subset=['Jmag','Hmag'], how='any')

    df_pm['KepMag'] = df_all['KepMag']
    df_pm['pmra'] = df_all['pmra']
    df_pm['pmdec'] = df_all['pmdec']

    df_pm['j_min_h'] = df_pm['Jmag'] - df_pm['Hmag']

    #Need to calculate reduced proper motion make sure to add in quadrature
    #H = m + 5log(mu) + 5 (y-axis)
    df_pm = df_pm.dropna(axis=0, subset=['KepMag','pmra','pmdec'], how='any')

    #use pmra and pmdec to get a total pm and conver mas/yr to arcsec/yr
    df_pm['pm'] = np.sqrt((((1/1000)*df_pm['pmra'])**2) + (((1/1000)*df_pm['pmdec'])**2))

    #pm is in mas/year so multiply by 1000
    df_pm['J'] = 5 + df_pm['Jmag'] + (5*(np.log(df_pm['pm'])))
    pdb.set_trace()

    J = df_pm['J']
    j_min_h = df_pm['j_min_h']

    dd = np.where(df_pm['logg'] >= 4.0)
    gg = np.where(df_pm['logg'] <= 3.0)
    m = np.where(np.logical_and(df_pm['logg'] > 3.0, df_pm['logg'] < 4.0))
    
    #Change the line below for dwarfs and giants
    giants = df_pm.iloc[gg]
    dwarfs = df_pm.iloc[dd]
    mid = df_pm.iloc[m]

    J_gg = giants['J']
    j_min_h_gg = giants['j_min_h']

    J_dd = dwarfs['J']
    j_min_h_dd = dwarfs['j_min_h']

    J_mid = mid['J']
    j_min_h_mid = mid['j_min_h']

    plt.plot(j_min_h_dd, J_dd, '.', c='blue', alpha=0.3, label='dwarf')
    plt.plot(j_min_h_gg, J_gg, '.', c='green', alpha=0.3, label='giant')
    plt.plot(j_min_h_mid, J_mid, '.', c='yellow', alpha=0.3, label='mid')
    plt.ylim(reversed(plt.ylim()))
    plt.xlabel('J - H')
    plt.ylabel('J')
    plt.grid(True)
    plt.legend(numpoints = 1)
    plt.savefig('graphs/%s/%s/%d_color_mag_colorized' %(campaign, folder, proposal))
    plt.show()

def make_temp_CM(campaign, proposal, folder):
    """
    proposal should be entered as an int
    campaign and folder are strings
    """
    df_all = pd.read_csv('csv_files/%s/master_search.csv' %campaign, low_memory=False)

    df_big_proposal = pd.read_csv('csv_files/%s/big_targets/prop_%d.csv' %(campaign, proposal), low_memory=False)
#Would want the above line to cycle through big_targets

    prop_id = df_big_proposal['EPIC ID']
    #pdb.set_trace()
    df_all = df_all.merge(df_big_proposal, left_on='EPIC', right_on='EPIC ID', how='inner')

    ww = np.where(df_all['Object type'] == 'STAR')
    df_all = df_all.iloc[ww]


    #initializing the data frame for calculating reduced proper motion
    df_pm = pd.DataFrame(columns=['Jmag','Hmag','KepMag','pmra','pmdec',
    'pm','j_min_h','H', 'Teff'])

    df_pm['Jmag'] = df_all['Jmag']
    df_pm['Hmag'] = df_all['Hmag']
    df_pm['Teff'] = df_all['Teff']


    #Removing any row that doesn't have a Jmag and Hmag value
    df_pm = df_pm.dropna(axis=0, subset=['Jmag','Hmag'], how='any')

    df_pm['KepMag'] = df_all['KepMag']
    df_pm['pmra'] = df_all['pmra']
    df_pm['pmdec'] = df_all['pmdec']

    df_pm['j_min_h'] = df_pm['Jmag'] - df_pm['Hmag']

    #Need to calculate reduced proper motion make sure to add in quadrature
    #H = m + 5log(mu) + 5 (y-axis)
    df_pm = df_pm.dropna(axis=0, subset=['KepMag','pmra','pmdec'], how='any')

    #use pmra and pmdec to get a total pm and conver mas/yr to arcsec/yr
    df_pm['pm'] = np.sqrt((((1/1000)*df_pm['pmra'])**2) + (((1/1000)*df_pm['pmdec'])**2))

    #pm is in mas/year so multiply by 1000
    df_pm['J'] = 5 + df_pm['Jmag'] + (5*(np.log(df_pm['pm'])))
    #pdb.set_trace()

    J = df_pm['J']
    j_min_h = df_pm['j_min_h']

    c = np.where(df_pm['Teff'] <= 4000)
    h = np.where(df_pm['Teff'] >= 6000)
    m = np.where(np.logical_and(df_pm['Teff'] > 4000, df_pm['Teff'] < 6000))
    #Change the line below for dwarfs and giants
    cold = df_pm.iloc[c]
    hot = df_pm.iloc[h]
    mid = df_pm.iloc[m]

    J_cold = cold['J']
    j_min_cold = cold['j_min_h']

    J_hot = hot['J']
    j_min_hot = hot['j_min_h']

    J_mid = mid['J']
    j_min_h_mid = mid['j_min_h']

    plt.plot(j_min_hot, J_hot, '.', c='blue', alpha=0.3)
    plt.plot(j_min_cold, J_cold, '.', c='red', alpha=0.3)
    plt.plot(j_min_h_mid, J_mid, '.', c='yellow', alpha=0.3)
    plt.ylim(reversed(plt.ylim()))
    plt.xlabel('J - H')
    plt.ylabel('J')
    plt.grid(True)
    plt.savefig('graphs/%s/%s/%d_CM_colorized' %(campaign, folder, proposal))
    plt.show()
