from pandas import DataFrame
from pandas import read_csv
import matplotlib.pyplot as plt
import pandas as pd

import sys
import matplotlib

# Enable inline plotting
# %matplotlib inline

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('matplotlib verstion ' + matplotlib.__version__)

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names, births))
print('BabyDataSet = ', BabyDataSet)

df = pd.DataFrame(data=BabyDataSet, columns=["Names", "Births"])
print('df = ', df)

df.to_csv('births1980.csv', index=False, header=False)

data = r"./births1980.csv"
df = pd.read_csv(data, names=["Names", "Births"])

print(df.Births.dtype)

Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)

record = df['Births'].max()
print('record = ', record)
print('names = ', df['Names'])
print('births = ', df['Births'])
print('max = ', df['Births'] == df['Births'].max())
print('find = ', df['Names'][df['Births'] == df['Births'].max()])
print('find head =', Sorted['Names'].head(1))


df['Births'].plot()

MaxValue = df['Births'].max()
print('MaxValue = ', MaxValue)
MaxName = df['Names'][df['Births'] == df['Births'].max()].values
print('MaxName = ', MaxName)
Text = str(MaxValue) + "-" + MaxName

plt.annotate(Text, xy=(1, MaxValue), xytext=(8,0), xycoords=('axes fraction', 'data'), textcoords='offset points')

print('The most popular name')

df[df['Births'] == df['Births'].max()]




