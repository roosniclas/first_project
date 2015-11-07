from collections import defaultdict
import pandas as pd
import numpy as np


file_name = 'lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv'

##population_dict = defaultdict(int)
##
##inputFile = open(file_name,'r')
##
##header = next(inputFile)
##for line in inputFile:
##    line = line.rstrip().split(',')
##    line[5] = int(line[5])
##    if line[1] == 'Total National Population':
##        population_dict[line[0]] += line[5]
##inputFile.close()
##
##with open('national_population.csv', 'w') as outputFile:
##    outputFile.write('continent,2010_population\n')
##
##    for k, v in population_dict.items():
##        outputFile.write(k + ',' + str(v) + '\n')
##
##

df = pd.read_csv(file_name)

df = df[df['ElevationZone'] == 'Total National Population']

table = df.groupby('Continent').agg({'Population2010' : np.sum, 'Population2100' : np.sum, 'LandArea' : np.sum})

table['PopulationDensity'] = table['Population2010'] / table['LandArea']

table['PopulationGrowth'] = ((table['Population2100'] / table['Population2010']) -1) * 100

print(table.sort_values('PopulationDensity', ascending=False))
