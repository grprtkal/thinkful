import collections
population_dict = collections.defaultdict(int)

with open("LECZ_Pop_Land_Data/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv", 'rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(",")
        population_2010 = int(line[5])
        population_2100 = int(line[6])

        print float(population_2010)

        if line[1] == "Total National Population":
            population_diff = population_2100 - population_2010
            population_dict[line[0]] = population_diff

with open("population_change.csv", "w") as outputFile:
    outputFile.write("continent,population_change\n")

    for k,v in population_dict.iteritems():
        outputFile.write(k + "," + str(v) + "\n")
