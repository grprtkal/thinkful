import pandas as pd
from scipy import stats


data = '''Region,Alcohol,Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# split every line into a string
data = data.split("\n")

# turn every string into list
# i.split(",")creates new string out of string at the comma
# for i in data iterates through the values of list and creates a list of out of the evaluation of the expression (
# i.split)
data = [i.split(",") for i in data]

# create dataframe
column_names = data[0]
data_rows = data[1::] #everything after row 1
df = pd.DataFrame(data_rows, columns=column_names)
print df['Alcohol']

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# find mean
df['Alcohol'].mean()
df['Tobacco'].mean()

# find median
df['Alcohol'].median()
df['Tobacco'].median()

# find mode
stats.mode(df["Tobacco"])





