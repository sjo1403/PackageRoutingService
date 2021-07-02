

class Truck:
    def __init__(self, ID, packages, route, mileage):
        self.ID = ID
        self.packages = packages
        self.route = route
        self.mileage = mileage

        def ID(self):
            print(ID)

        def packages(self):
            print(packages)

        def route(self):
            print(route)

        def mileage(self):
            print(mileage)


def mileage(Truck):
    totalMileage = 0
    for i in Truck.mileage:
        totalMileage += float(i)

    print(totalMileage)
