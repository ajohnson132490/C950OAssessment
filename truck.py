from datetime import timedelta
import csv

class Truck:
    # Creating constants for the truck
    CONST_SPEED = 18
    CONST_MAX_PACKAGES = 16
    CONST_HUB_ADDRESS = "4001 South 700 East"

    # Creating some data holders
    load = []
    address_list = []
    distance_data = [[0 for x in range(26)] for y in range(26)]

    def __init__(self, id):
        self.id = id
        self.current_time = timedelta(hours = 8, minutes = 0, seconds = 0)
        self.current_address = self.CONST_HUB_ADDRESS

        # Populate data needed for other functions
        self.populateAddressesAndDistances()

    def populateAddressesAndDistances(self):
        # Get all the addresses in an array
        with open('Resources/addresses.csv') as address_file:
            reader = csv.reader(address_file, delimiter = ",")

            # Get every address in the csv file
            for address in reader:
                full_address = address[0].split("\n")
                street_address = full_address[1].strip()
                self.address_list.append(street_address)

        # Get all the distances in a 2d array
        with open('Resources/distances.csv') as distance_file:
            reader = csv.reader(distance_file, delimiter = ",")

            # Get every row in the csv file 
            row_index = 0
            for row in reader:
                for j in range(26):
                    if row[j] != '':
                        # Put it in a table format
                        self.distance_data[row_index][j] = float(row[j])
                        self.distance_data[j][row_index] = float(row[j])
            row_index += 1

    def distanceBetween(self, address1, address2):
        return self.distance_data[self.address_list.index(address1), self.address_list.index(address2)]

    def loadPackages(self, hash, list):
        ordered_list = self.buildRoute(list)
        for package in ordered_list: 
            package.loaded_timestamp = self.current_time
            package.status = "En route"
            self.load.append(package)

    def buildRoute(self, hash, list):
        nearest_pkg = None
        nearest_pkg_dist = None
        ordered_list = []
        for p in list:
            for package_id in list:
                package = hash.get(package_id)
                if nearest_pkg is None:
                    nearest_pkg = package
                    nearest_pkg_dist = self.distanceBetween(nearest_pkg.address, p.address)
                else:
                    new_pkg_dist = self.distanceBetween(package.address, p.address)

                    if new_pkg_dist < nearest_pkg_dist:
                        nearest_pkg = package
                        nearest_pkg_dist = new_pkg_dist
            ordered_list.append(nearest_pkg)
        return ordered_list
