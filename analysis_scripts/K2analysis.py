import csv
import matplotlib.pyplot as plt
import numpy as np

mass = []
t = []
radius = []
kepMag = []
kMag = []

lst_to_append = [mass, t, radius, kepMag, kMag]
csv_strs = ['mass.csv', 'tEff.csv', 'radius.csv', 'kepMag.csv', 'kMag.csv']

i = 0
#populates all the lists with the correct values
for filename in csv_strs:
    with open(filename, 'rb') as m:
    #using csv reader to put data into arrays
        reader = csv.reader(m)

        for row in reader:
        #must turn row with string obj into float
            str1 = row[0]
            if filename == 'tEff.csv':
                val = int(str1)
                t.append(val)
            else:
                val = float(str1)
                lst_to_append[i].append(val)
    i += 1

#change array that goes into plt function
#print max(kMag)
plt.xlabel('Mass')
#weights = np.ones_like(kMag)/float(len(kMag))
plt.grid(True)
plt.hist(mass, bins = 40)
plt.show()
