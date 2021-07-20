from datetime import timedelta
import HashTable
import Trucks

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, truck, status="EN-ROUTE"):
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


def checkStatus(hour, minute, packageID =None):
    tf = timedelta(hours=hour, minutes=minute)
    print("PACKAGE STATUS AS OF " + str(tf) + ":\n")

    for truck in Trucks.trucks:

        hour = int(truck.start / 60)
        minute = truck.start % 60

        ti = timedelta(hours=hour, minutes=minute)
        delta = tf - ti
        timeElapsed = delta.total_seconds() / 60

        currentMile = (timeElapsed * 0.3)

        totalMiles = 0
        for d in truck.distance:
            totalMiles += d

        if currentMile <= 0:
            for package in truck.packages:
                setStatus(package, "AT-HUB")
            continue

        elif currentMile > totalMiles:
            deliverPackage(truck, len(truck.distance))
            continue

        else:
            sum = truck.distance[0]
            i = 1
            index = 0

            while sum < currentMile:
                index = i
                sum += truck.distance[index]
                i += 1

            deliverPackage(truck, index)

    if packageID == None:
        for i in range(1, 41):
            value = packages.getValue(i)
            info(value)

    else:
        value = packages.getValue(packageID)
        info(value)


def deliverPackage(truck, index):
    for i in range(index + 1):
        for val in range(1, 41):
            value = packages.getValue(val)

            if getAddress(value) in truck.route[i]:
                sum = 0
                for m in truck.distance[:i]:
                    sum += m

                deliveryTime = str((sum / 18 * 60) + truck.start)
                hour = int(float(deliveryTime) / 60)
                minute = float(deliveryTime) % 60
                t = timedelta(hours=hour, minutes=minute)
                setStatus(value, "DELIVERED AT: " + str(t))

            else:
                continue


def setStatus(Package, status):
    Package.status = status


def getAddress(package):
    return package.address

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
