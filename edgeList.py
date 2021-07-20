import csv

data = open("distances.csv", 'r')   # read data from distance table
rawData = csv.reader(data)

locations = []  # parse data to build list of locations

for line in rawData:
    locations.append(line)

data.close()

data2 = open("miles2.csv", 'r') # read data from miles table
rawMiles = csv.reader(data2)

miles = []  # parse data to build list of distances

for line in rawMiles:
    for string in line:
        trim = string.strip().split('\t')
        miles.append(trim)

weightedEdgeList = []   # build location/distance edgelist from location and distance lists

for i in range(0,27):   # columns
    for j in range(0, 27):   # rows
        two_list = []  # list of paired locations
        trip_list = []   # list of paired locations with respective distance

        two_list.append(locations[i])
        two_list.append(locations[j])

        trip_list.append(float(miles[j][i]))    #f inds the distance between locations j and i
        trip_list.append(two_list)
        weightedEdgeList.append(trip_list)

# Nearest Neighbor algorithm implemented to create delivery route (path)
nextLoc = weightedEdgeList[0][1][0]     # the hub (WGU) is where the delivery path starts
path = [nextLoc]
distanceTraveled = []
tempList = []

while len(path) < 27:
    for item in weightedEdgeList:
        if item[1][0] == nextLoc:   # creates a tempList where the starting vertices are the same
            tempList.append(item)

    adjustedList = sorted(tempList)     # creates new list from sorted tempList, used to find the shortest paths
    tempList.clear()

    i = 0
    while i < len(adjustedList):
        if adjustedList[i][1][1] not in path:
            nextLoc = adjustedList[i][1][1]
            mileage = adjustedList[i][0]
            path.append(nextLoc)    # add ending vertex to the path
            distanceTraveled.append(mileage)
            i = 26

        else:
            i += 1
            continue

"""""
for i in path:
    print(str(i))
floatDistance = 0
for i in distanceTraveled:
    floatDistance += float(i)

print("Miles traveled: " + str(floatDistance))
print(distanceTraveled)
"""
