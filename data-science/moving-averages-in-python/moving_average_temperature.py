from import pandas as pd

# load the csv file (Monthly average air temperatures of the city of Barcelona
# since 1780) into a pandas data frame
df_temperature = pd.read_csv(
    'temperaturesbarcelonadesde1780.csv', encoding='utf-8')

# visualize first 5 rows
df_temerature.head()
