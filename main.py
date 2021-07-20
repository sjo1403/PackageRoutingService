# Shantel Johnson
# 001344693

import Packages

print("Welcome to the WGUPS ROUTING PROGRAM.\n"
      "To check the package status, please enter the hour of the time you wish to check, followed by the minute.\n"
      "(Optional) You may also input the Package ID to check the status of a specific package.\n\n")

hour = int(input("Please enter the hour: "))
minute = int(input("Please enter the minute: "))
package = input("(Optional) Enter the Package ID: ")

if package != "":   # Package ID was entered, check status of specific package
    Packages.checkStatus(hour, minute, int(package))
else:   # No Package ID was entered, check status of all packages
    Packages.checkStatus(hour, minute)
