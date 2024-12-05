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
    distance_data = [[0 for x in range(27)] for y in range(27)]

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
                for j in range(27):
                    if row[j] != '':
                        # Put it in a table format
                        self.distance_data[row_index][j] = float(row[j])
                        #print(float(row[j]))
                        self.distance_data[j][row_index] = float(row[j])
                    else: 
                        self.distance_data[row_index][j] = float(99.9)
                row_index += 1

            s = ""
            for row in range(27):
                for j in range(27):
                    s += (str(self.distance_data[row][j]) + ", ")
                #print(f"Row {row}: {s}")
                s = ""

    def distanceBetween(self, address1, address2):
        return self.distance_data[self.address_list.index(address1)][self.address_list.index(address2)]

    def loadPackages(self, hash, list):
        ordered_list = self.buildRoute(hash, list)
        for package in ordered_list[:-1]: 
            package.loaded_timestamp = self.current_time
            package.status = "En route"
            self.load.append(package)

    def buildRoute(self, hash, lst):
        # THiS FINDS THE NEXT NEAREST PACKAGE, BUT DOESN'T CHECK FOR THE NEAREST PACKAGE TO THE CURRENT LOCATION
        nearest_pkg = None
        nearest_pkg_dist = 99.9
        ordered_list = []
        first_pkg = True
        adj_list = list(lst)
        for p in lst:
            cur_pkg = hash.get(p)

            if (first_pkg):
                for package_id in adj_list:
                    package = hash.get(package_id)
                    temp_dist = self.distanceBetween(package.address, self.current_address)
                    if temp_dist < nearest_pkg_dist:
                        nearest_pkg = package
                        nearest_pkg_dist = temp_dist
                        #print(f"new nearest pkg dist: {nearest_pkg_dist} on pkg {package.getId()}")

                first_pkg = False

            for package_id in adj_list:
                if package_id != p:
                    package = hash.get(package_id)
                    if nearest_pkg is None:
                        nearest_pkg = package
                        nearest_pkg_dist = self.distanceBetween(nearest_pkg.address, cur_pkg.address)
                    else:
                        new_pkg_dist = self.distanceBetween(package.address, cur_pkg.address)

                        if new_pkg_dist < nearest_pkg_dist:
                            nearest_pkg = package
                            nearest_pkg_dist = new_pkg_dist
            ordered_list.append(nearest_pkg)
            try:
                adj_list.remove(nearest_pkg.getId())
                #print("final nearest distance: ", nearest_pkg_dist, " between cur_pkg: ", cur_pkg.getId(), " and package: ", nearest_pkg.getId())
            except:
                #adj_list is empty
                nearest_pkg = None
            nearest_pkg = None
        str = ""
        ordered_list.pop()
        ordered_list.reverse()
        for item in ordered_list:
            str += f"{item.getId()}"
            str += " --> "
        print(str)
        return ordered_list
