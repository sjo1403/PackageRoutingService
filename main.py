

import Packages

#read data from packages file
import csv
data = open("packageFile.csv", 'r')
rawData = csv.reader(data)

packageData = []

for line in rawData:
    for string in line:
        trim = string.strip().split('\t')
        packageData.append(trim)

for line in range(1,40):
    packageID = packageData[line][0]
    address = packageData[line][1]
    city = packageData[line][2]
    state = packageData[line][3]
    zip = packageData[line][4]
    deadline = packageData[line][5]
    mass = packageData[line][6]
    #notes = packageData[line][7]

    package = Packages.Package(packageID,address,city,state,zip,deadline,mass)
    Packages.addPackage(package)

dummy = Packages.Package(0,"Maple Ridge","City","State",00000,"EOB",100,"THIS IS A DUMMY, RETURN TO WORK TOMORROW")

print(dummy.notes)
