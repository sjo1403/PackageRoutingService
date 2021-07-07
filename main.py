import HashTable
import Packages

#read data from packages file
import csv

import Trucks

data = open("packageFile.csv", 'r')
rawData = csv.reader(data)

packageData = []

for line in rawData:
    for string in line:
        trim = string.strip().split('\t')
        packageData.append(trim)

#create HashTable instance and insert packages

packages = HashTable.HashTable()

i = 1   #int i used for key in HashTable
for line in range(1,41):    #create Package objects from packageFile data
    packageID = packageData[line][0]
    address = packageData[line][1]
    city = packageData[line][2]
    state = packageData[line][3]
    zip = packageData[line][4]
    deadline = packageData[line][5]
    mass = packageData[line][6]
    truck = packageData[line][7]

    Package = Packages.Package(packageID,address,city,state,zip,deadline,mass,truck)
    packages.hashInsert(i, Package)
    Trucks.loadPachages(Package)

    i += 1
