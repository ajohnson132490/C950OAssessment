class Hash():
    def __init__(self):
        # Private attributes for buckets and table
        self.__bucket = 7
        self.__table = [[] for _ in range(self.__bucket)]

    # The sorting hash function using a package object or a package id
    def __hashFunction(self, package):
        if isinstance(package, int):
            return (package % self.__bucket)
        return (package.getId() % self.__bucket)
    
    # Inserts an item into the list on a given index
    def insertItem(self, package):
        index = self.__hashFunction(package)
        self.__table[index].append(package)

    # Removes an item from the list on a given index
    def removeItem(self, package):
        index = self.__hashFunction(package)
        
        if package not in self.__table[index]:
            return
        
        self.__table[index].remove(package)
        
    # Gets an individual package by the id
    def get(self, id):
        index = self.__hashFunction(id)
        
        for p in self.__table[index]:
            if p.getId() == id:
                return p
            
