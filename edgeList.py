

#read data from distance table
import csv
import token

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
weightedEdgeList = []

for i in range(0,27):   #columns
    for j in range(i + 1,27):   #rows
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
i = 1

while i in range(27):

    for item in weightedEdgeList:
        if item[1][0] == nextLoc:   #creates a tempList where the starting verticies are the same
            tempList.append(item)

    if len(tempList) == 0:  #if the tempList is empty, go to the last location on the path and find the next closest location
        nextLoc = path[-1]
#        print(nextLoc)
        i +=1

    else:
        adjustedList = sorted(tempList)
        tempList.clear()

        for set in adjustedList:
            nextLoc = set[1][1]
            mileage = set[0]

            if nextLoc in path:     #loops through code block until a unique ending vertex is found
                continue

            else:
        #        print(nextLoc)
                path.append(nextLoc)    #add ending vertex to the path
                distanceTraveled.append(mileage)
                i += 1

for i in path:
    print(i)

floatDistance = 0
for i in distanceTraveled:
    floatDistance += float(i)

print("Miles traveled: " + str(floatDistance))
print(distanceTraveled)
