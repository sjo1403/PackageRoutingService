

class Package:
    def __init__(self, packageID, address, city, state, zip, deadline, mass, notes="--"):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes

        def packageID(self):
            print(packageID)
        def address(self):
            print(address)
        def city(self):
            print(city)
        def state(self):
            print(state)
        def zip(self):
            print(zip)
        def deadline(self):
            print(deadline)
        def mass(self):
            print(mass)
        def notes(self):
            print(notes)

packages = []

def addPackage(Package):
    packages.append(Package)

def getPackages():
    for line in packages:
        print(line)