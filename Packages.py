import HashTable
import Trucks

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, truck, status="AT-HUB"):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.truck = truck
        self.status = status


def info(Package):
    info = "Package ID: " + str(Package.ID) + "\t" + str(Package.address) + "\t" + str(Package.city) + ", " + \
           str(Package.state) + "\t" + str(Package.zip) + "\tDELIVER BY: " + str(Package.deadline) + "\t" \
           + str(Package.mass) + " pounds\t" + str(Package.status)
    print(info)


def checkStatus(currentTime):
    print("Time: " + str(currentTime))

    for truck in Trucks.trucks:

        timeElapsed = (currentTime - truck.start)
        currentMile = (timeElapsed * 0.3)

        if currentMile <= 0:
            continue

        else:
            sum = 0
            index = 0
            while sum < currentMile:
                sum += truck.distance[index]
                index += 1

            deliverPackage(truck, index)

    for i in range(1, 41):
        value = packages.getValue(i)
        info(value)


def deliverPackage(truck, index):
    for i in range(1, 41):
        value = packages.getValue(i)

        for t in truck.packages[:index - 1]:
            if t == value:
                setStatus(value)


def setStatus(Package):
    Package.status = "Delivered"



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

    package = Package(packageID, address, city, state, zip, deadline, mass, truck)
    packages.hashInsert(i, package)
    Trucks.loadPackages(package)

    i += 1
