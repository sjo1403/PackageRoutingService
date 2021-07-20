class Truck:
    def __init__(self, ID, name, packages, start, route, distance):     # create instance of Truck object
        self.ID = ID
        self.name = name
        self.packages = packages
        self.start = start
        self.route = route
        self.distance = distance


trucks = []

# list of packages in truck
T1Packages = []
T2Packages = []
T11Packages = []
T22Packages = []

# list of truck routes
T1Route = \
 ['Western Governors University 4001 South 700 East Salt Lake City UT 84107',
'Cottonwood Regional Softball Complex 4300 S 1300 E',
'Holiday City Office 4580 S 2300 E',
'City Center of Rock Springs 5383 South 900 East #104',
'Wheeler Historic Farm 6351 South 900 East',
'Murray City Museum 5025 State St',
'Housing Auth. of Salt Lake County 3595 Main St',
'Salt Lake City Division of Health Services 177 W Price Ave',
'West Valley Prosecutor 3575 W Valley Central Station bus Loop',
'Western Governors University 4001 South 700 East Salt Lake City UT 84107']

T2Route = \
 ['Western Governors University 4001 South 700 East Salt Lake City UT 84107',
'Third District Juvenile Court 410 S State St',
'Council Hall 300 State St',
'Salt Lake City Ottinger Hall 233 Canyon Rd',
'Salt Lake City Streets and Sanitation 2010 W 500 S',
'International Peace Gardens 1060 Dalton Ave S',
'Taylorsville-Bennion Heritage City Gov Off 1488 4800 S',
'Valley Regional Softball Complex 5100 South 2700 West',
'Taylorsville City Hall 2600 Taylorsville Blvd',
'Western Governors University 4001 South 700 East Salt Lake City UT 84107']

T11Route = \
 ['Western Governors University 4001 South 700 East Salt Lake City UT 84107',
'City Center of Rock Springs 5383 South 900 East #104']


T22Route = \
 ['Deker Lake 2300 Parkway Blvd',
'Redwood Park 3060 Lester St',
'Salt Lake County Mental Health 3148 S 1100 W',
'Salt Lake County/United Police Dept 3365 S 900 W',
'Utah DMV Administrative Office 380 W 2880 S',
'South Salt Lake Police 2835 Main St',
'South Salt Lake Public Works 195 W Oakland Ave',
'Columbus Library 2530 S 500 E',
'Sugar House Park 1330 2100 S',
'Rice Terrace Pavilion Park 600 E 900 South',
'Third District Juvenile Court 410 South State St']

# list of truck Distances in miles
T1Dist = [1.9, 2.0, 3.4, 1.3, 3.1, 2.3, 0.5, 1.4, 7.6]
T2Dist = [6.5, 1.0, 0.6, 4.2, 1.6, 6.4, 0.6, 0.4, 8.6]
T11Dist = [2.4]
T22Dist = [1.6, 1.3, 0.6, 1.7, 1.0, 0.8, 1.5, 1.6, 2.8, 1.8]


def loadPackages(Package):  # load packages onto each truck
    if Package.truck == "T1":
        T1Packages.append(Package)

    elif Package.truck == "T2":
        T2Packages.append(Package)

    elif Package.truck == "T11":
        T11Packages.append(Package)

    else:
        T22Packages.append(Package)


#   create truck objects from information above
truck1 = Truck("T1", "Truck 1", T1Packages, 480, T1Route, T1Dist)
truck2 = Truck("T2", "Truck 2", T2Packages, 480, T2Route, T2Dist)
truck11 = Truck("T11", "Truck 1", T11Packages, 559, T11Route, T11Dist)
truck22 = Truck("T22", "Truck 2", T22Packages, 580, T22Route, T22Dist)
trucks.append(truck1)
trucks.append(truck2)
trucks.append(truck11)
trucks.append(truck22)
