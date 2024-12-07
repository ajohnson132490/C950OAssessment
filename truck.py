from datetime import timedelta
import csv

class Truck:
    # Creating constants for the truck
    CONST_SPEED = 18
    CONST_MAX_PACKAGES = 16
    CONST_HUB_ADDRESS = "4001 South 700 East"    

    def __init__(self, id):
        self.id = id
        self.current_time = timedelta(hours = 8, minutes = 0, seconds = 0)
        self.current_address = self.CONST_HUB_ADDRESS
        self.load = []
        self.delivery_timestamps = []
        self.address_list = []
        self.distance_data = [[0 for x in range(27)] for y in range(27)]
        self.mileage = 0.0

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

            
    def distanceBetween(self, address1, address2):
        return self.distance_data[self.address_list.index(address1)][self.address_list.index(address2)]

    def loadPackages(self, hash, lst):
        ordered_list = self.buildRoute(hash, lst)
        for package in ordered_list: 
            package.loaded_timestamp = self.current_time
            package.status = "En route"
            package.onTruck = self.id
            self.load.append(package.getId())

    def buildRoute(self, hash, lst):
        temp_address = None
        nearest_pkg = None
        nearest_pkg_dist = 99.9
        ordered_list = []
        adj_list = list(lst)
        first_pkg = 0

        for package_id in lst:
            package = hash.get(package_id)
            temp_dist = self.distanceBetween(package.address, self.current_address)
            if temp_dist < nearest_pkg_dist:
                nearest_pkg = package
                nearest_pkg_dist = temp_dist
                #print(f"new nearest pkg dist: {nearest_pkg_dist} on pkg {package.getId()}")
            first_pkg = nearest_pkg.getId()
            temp_address = nearest_pkg.address
        ordered_list.append(nearest_pkg)
        try:
            adj_list.remove(int(first_pkg))
        except:
            del first_pkg
        
        nearest_pkg = None

        for p in lst:
            nearest_pkg_dist = 99.9
            try:
                for package_id in adj_list:
                    new_package = hash.get(package_id)
                    new_pkg_dist = self.distanceBetween(new_package.address, temp_address)

                    if new_pkg_dist < nearest_pkg_dist:
                        nearest_pkg = new_package
                        nearest_pkg_dist = new_pkg_dist
                
                ordered_list.append(nearest_pkg)
                adj_list.remove(nearest_pkg.getId())
                temp_address = nearest_pkg.address
                #print("final nearest distance: ", nearest_pkg_dist, " between cur_pkg: ", p, " and package: ", nearest_pkg.getId())
            except:
                #adj_list is empty
                del nearest_pkg_dist

        ordered_list.pop()

        return ordered_list
    
    def deliverPackages(self, hash):
        #print(self.load)
        # Iterate through all package in the current load
        for package_id in self.load:
            package = hash.get(package_id)
            str = ""
            #print(f"Current PKG: {package.getId()}")

            # Update the mileage and time
            temp_dist = self.distanceBetween(self.current_address, package.address)
            #print("TEMP DIST: ", temp_dist)
            self.mileage += temp_dist
            self.current_time += timedelta(minutes=(temp_dist / self.CONST_SPEED * 60))
            self.delivery_timestamps.append([self.mileage, self.current_time])

            # Deliver the package
            package.status = "Delivered"
            package.delivered_timestamp = self.current_time

            # Update the current address
            self.current_address = package.address
        # Clear out the load list
        #print(f"\nTRUCK {self.id} DELIVERY ROUTE COMPLETE\n")
        self.load.clear()
        
        # Return to the hub
        dist_from_hub = self.distanceBetween(self.current_address, self.CONST_HUB_ADDRESS)
        self.current_time += timedelta(minutes=(dist_from_hub / self.CONST_SPEED * 60))
        self.delivery_timestamps.append([self.mileage, self.current_time])

