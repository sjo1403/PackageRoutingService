

#read data from distance table
import csv
import random
import token

data = open("distances.csv", 'r')
rawData = csv.reader(data)

#parse data to build list of locations
locations = []

for line in rawData:
    locations.append(line)

data.close()

#read data from miles table
data2 = open("miles2.csv", 'r')
rawMiles = csv.reader(data2)

#parse data to build list of distances
miles = []

for line in rawMiles:
    for string in line:
        trim = string.strip().split('\t')
        miles.append(trim)

#build location/distance edgelist from location and distance lists
weightedEdgeList = []

for i in range(0,27):   #columns
    for j in range(0, 27):   #rows
        two_list = []  #list of paired locations
        trip_list = []   #list of paired locations with respective distance

        two_list.append(locations[i])
        two_list.append(locations[j])

        trip_list.append(miles[j][i])    #finds the distance between locations j and i
        trip_list.append(two_list)
        weightedEdgeList.append(trip_list)

#greedy algorithm implemented to create path
nextLoc = weightedEdgeList[0][1][0]     #the hub (WGU) is where the delivery path starts
path = [nextLoc]
distanceTraveled = []
tempList = []

while len(path) < 27:
    for item in weightedEdgeList:
        if item[1][0] == nextLoc:   #creates a tempList where the starting verticies are the same
            tempList.append(item)

    adjustedList = sorted(tempList)
    tempList.clear()

    i = 0
    while i < len(adjustedList):
        if adjustedList[i][1][1] not in path:
            nextLoc = adjustedList[i][1][1]
            mileage = adjustedList[i][0]
            path.append(nextLoc)    #add ending vertex to the path
            distanceTraveled.append(mileage)
            i = 26

        else:
            i += 1
            continue

for i in path:
    print(i)

floatDistance = 0
for i in distanceTraveled:
    floatDistance += float(i)

print("Miles traveled: " + str(floatDistance))
print(distanceTraveled)
