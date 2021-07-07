import Packages

class HashTable(object):
    def __init__(self, length = 41):
        self.array = [None] * length

    def hashInsert(self, key, value):
        index = key
        self.array[index] = key, value

    def hashSearch(self, key):
        index = key
        if self.array[index] is None:
            print("Key Error: Package ID '0' does not exist.")

        else:
            package = self.array[index][1]
            Packages.info(package)
