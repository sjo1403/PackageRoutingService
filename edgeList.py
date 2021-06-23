

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

#build location/distance edgelist from location and distance lists
edgeList = []

for i in range(0,27):   #columns
    for j in range(i + 1,27):   #rows
        two_tup = []  #list of paired locations
        trip_tup = []   #list of paired locations with respective distance

        two_tup.append(locations[i])
        two_tup.append(locations[j])
        trip_tup.append(miles[j][i])    #finds the distance between locations j and i
        trip_tup.append(two_tup)
        edgeList.append(trip_tup)

adjustedList = sorted(edgeList)

greedy = []
mileage = 0

for i in range(351):
    if adjustedList[i][1][0] not in greedy:
        greedy.append(adjustedList[i][1][0])
        floatingMiles = float(adjustedList[i][0])
        mileage += floatingMiles
        print(adjustedList[i][1])

print(len(greedy))
print(mileage)
