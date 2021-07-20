import Packages


class HashTable(object):
    def __init__(self, length = 41):    # create instance of HashTable object, includes space for a default of 41 packages
        self.array = [None] * length

    def hashInsert(self, key, value):   # add values to HashTable
        index = key
        self.array[index] = key, value

    def hashSearch(self, key):  # lookup package; if key exists, return package info
        index = key
        if self.array[index] is None:
            print("Key Error: Package ID '0' does not exist.")

        else:
            package = self.array[index][1]
            Packages.info(package)

    def getValue(self, key):    # lookup key; if key exists, return value
        index = key
        if self.array[index] is None:
            print("Key Error: Package ID '0' does not exist.")

        else:
            return self.array[index][1]
