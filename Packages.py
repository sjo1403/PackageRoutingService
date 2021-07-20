from datetime import timedelta
import csv
import HashTable
import Trucks

class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, truck, status="EN-ROUTE"):    # create instance of Package object
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.truck = truck
        self.status = status


def info(Package):  # returns components of package object, used in checkStatus method
    info = "Package ID: " + str(Package.ID) + "\t" + \
           str(Package.address) + "\t" + \
           str(Package.city) + ", " + \
           str(Package.state) + "\t" + \
           str(Package.zip) + \
           "\tDELIVER BY: " + str(Package.deadline) + "\t" + \
           str(Package.mass) + " pounds\t" + \
           str(Package.status)

    print(info)


def checkStatus(hour, minute, packageID =None): # returns the status of one or all packages, based on the time input
    tf = timedelta(hours=hour, minutes=minute)
    print("PACKAGE STATUS AS OF " + str(tf) + ":\n")

    for truck in Trucks.trucks:
        hour = int(truck.start / 60)    # convert datetime format into minutes elapsed (timeElapsed)
        minute = truck.start % 60
        ti = timedelta(hours=hour, minutes=minute)
        delta = tf - ti
        timeElapsed = delta.total_seconds() / 60
        currentMile = (timeElapsed * 0.3)
        totalMiles = 0  # total miles traveled by 1 truck going 18mph

        for d in truck.distance:
            totalMiles += d

        if currentMile <= 0:    # truck has not departed, so change package status to "AT-HUB"
            for package in truck.packages:
                setStatus(package, "AT-HUB")
            continue

        elif currentMile > totalMiles:  # all packages in the truck were delivered before reaching totalMiles
                                        # change package status for all packages to "DELIVERED"
            deliverPackage(truck, len(truck.distance))

        else:   # truck has departed, but not all packages have been delivered
                # change package status to "DELIVERED" up to the truck's current location
            sum = truck.distance[0]
            i = 1
            index = 0

            while sum < currentMile:
                index = i
                sum += truck.distance[index]
                i += 1

            deliverPackage(truck, index)

    if packageID == None:   #return status for all packages
        for i in range(1, 41):
            value = packages.getValue(i)
            info(value)

    else:   # return status for a single package
        value = packages.getValue(packageID)
        info(value)

    totalMilesDriven = 0
    for i in milesDriven:   # calculate total miles driven by all trucks
        totalMilesDriven += i

    print("\nTotal miles driven: " + str(totalMilesDriven))


milesDriven = [] # total miles driven by each truck


def deliverPackage(truck, index):   # set delivery status of a package(s) in a given truck to "DELIVERED"
    total = 0

    for d in truck.distance[:index + 1]:
        total += d

    milesDriven.append(total)

    for i in range(index + 1):
        for val in range(1, 41):
            value = packages.getValue(val)

            sum = 0
            if getAddress(value) in truck.route[i]:
                for m in truck.distance[:i]:
                    sum += m

                deliveryTime = str((sum / 18 * 60) + truck.start)   # convert the timeElapsed into datetime format
                hour = int(float(deliveryTime) / 60)
                minute = float(deliveryTime) % 60
                t = timedelta(hours=hour, minutes=minute)
                setStatus(value, "DELIVERED AT: " + str(t))


def setStatus(Package, status):     # set the status of a given package, used in deliverPackage method
    Package.status = status


def getAddress(package):    # return the address of a given package, used in deliverPackage method
    return package.address


data = open("packageFile.csv", 'r')     # read data from packages file
rawData = csv.reader(data)

packageData = []

for line in rawData:
    for string in line:
        trim = string.strip().split('\t')
        packageData.append(trim)

packages = HashTable.HashTable()    # create HashTable instance and insert packages

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
    packages.hashInsert(i, package) # insert packages into HashTable
    Trucks.loadPackages(package)

    i += 1
