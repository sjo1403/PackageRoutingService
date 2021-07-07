class Package:
    def __init__(self, ID, address, city, state, zip, deadline, mass, truck):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.truck = truck

        def ID(self):
            print(ID)
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
        def truck(self):
            print(truck)

def info(Package):
    info = "Package ID: " + str(Package.ID) + "\t" + str(Package.address) + "\t" + str(Package.city) + ", " + \
           str(Package.state) + "\t" + str(Package.zip) + "\tDELIVER BY: " + str(Package.deadline) + "\t" \
           + str(Package.mass) + " pounds"
    print(info)
