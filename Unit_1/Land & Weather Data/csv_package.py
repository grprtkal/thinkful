import csv

with open("LECZ_Pop_Land_Data/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_codebook.csv", "r") as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print line



