class Truck:
    def __init__(self, ID, packages, route):
        self.ID = ID
        self.packages = packages
        self.route = route

        def ID(self):
            print(ID)

        def packages(self):
            print(packages)

        def route(self):
            print(route)

#list of packages to build Truck object
T1Packages = []
T2Packages = []
T3Packages = []

#list of routes to build Truck object
T1Route = []
T2Route = []
T3Route = []

def loadPachages(Package):
    if Package.truck == "T1":
        T1Packages.append(Package)
        T1Route.append(Package.address)

    elif Package.truck == "T2":
        T2Packages.append(Package)
        T2Route.append(Package.address)

    else:
        T3Packages.append(Package)
        T3Packages.append(Package.address)
