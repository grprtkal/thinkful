import collections
population_dict = collections.defaultdict(int)

with open("LECZ_Pop_Land_Data/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv", 'rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(",")
        line[5] = int(line[5])
        if line[1] == "Total National Population":
            population_dict[line[0]] += line[5]

with open("national_population.csv", "w") as outputFile:
        outputFile.write("continent,2010_population\n")

        for k,v in population_dict.iteritems(): #iteritems iterates through key-value pairs in dictionary
            outputFile.write(k + "," + str(v) + "\n")

