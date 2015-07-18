import pandas as pd

input_dataframe = pd.read_csv("LECZ_Pop_Land_Data/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv")
input_with_head = input_dataframe.head()

print(input_with_head)
# print(input_dataframe)
