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

            currentLocation = truck.route[index - 1]
            print(str(truck.ID) + ": " + str(currentLocation))
