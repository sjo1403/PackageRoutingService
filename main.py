import HashTable
import Packages
import Trucks

# read data from packages file
import csv

data = open("packageFile.csv", 'r')
rawData = csv.reader(data)

packageData = []

for line in rawData:
    for string in line:
        trim = string.strip().split('\t')
        packageData.append(trim)

# create HashTable instance and insert packages
packages = HashTable.HashTable()

i = 1  # int i used for key in HashTable
for line in range(1, 41):  # create Package objects from packageFile data
    packageID = packageData[line][0]
    address = packageData[line][1]
    city = packageData[line][2]
    state = packageData[line][3]
    zip = packageData[line][4]
    deadline = packageData[line][5]
    mass = packageData[line][6]
    truck = packageData[line][7]

    Package = Packages.Package(packageID, address, city, state, zip, deadline, mass, truck)
    packages.hashInsert(i, Package)
    Trucks.loadPackages(Package)

    i += 1

truck1 = Trucks.Truck("Truck 1", Trucks.T1Packages, 0, Trucks.T1Route, Trucks.T1Dist)
truck2 = Trucks.Truck("Truck 2", Trucks.T2Packages, 0, Trucks.T2Route, Trucks.T2Dist)
truck11 = Trucks.Truck("Truck 1", Trucks.T11Packages, 90, Trucks.T11Route, Trucks.T11Dist)
truck22 = Trucks.Truck("Truck 2", Trucks.T22Packages, 65, Trucks.T22Route, Trucks.T22Dist)
Trucks.trucks.append(truck1)
Trucks.trucks.append(truck2)
Trucks.trucks.append(truck11)
Trucks.trucks.append(truck22)

Packages.checkStatus(42)
