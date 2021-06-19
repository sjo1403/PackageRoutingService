

#read data from distance table
import csv
data = open("distances.csv", 'r')
rawData = csv.reader(data)

#parse data to build list of locations
locations = []

for line in rawData:
    locations.append(line)

data.close()

#read data from miles table
data2 = open("miles.csv", 'r')
rawMiles = csv.reader(data2)

#parse data to build list of distances
miles = []

for line in rawMiles:
    for string in line:
        trim = string.strip().split('\t')
        miles.append(trim)

#build distance/location matrix from location and distance lists
matrix = []

for i in range(0,27):   #columns
    for j in range(i + 1,27):   #rows
        pairs = []  #list of paired locations
        triplets = []   #list of paired locations with respective distance

        pairs.append(locations[i])
        pairs.append(locations[j])
        triplets.append(pairs)
        triplets.append(miles[j][i])    #finds the distance between locations j and i
        print(pairs)
        print(miles[j][i])
        print("\n")
        matrix.append(triplets)
