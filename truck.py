from datetime import timedelta

class Truck:
    speed = 18
    max_packages = 16
    load = []

    def __init__(self, id):
        self.id = id
        self.current_time = timedelta(hours = 8, minutes = 0, seconds = 0)

    def loadPackages(self, hash, list):
        for id in list: 
            package = hash.get(id)
            package.loaded_timestamp = self.current_time
            package.status = "En route"
            self.load.append(package)