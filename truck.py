from datetime import timedelta
import csv

class Truck:
    # Creating constants for the truck
    CONST_SPEED = 18
    CONST_MAX_PACKAGES = 16
    CONST_HUB_ADDRESS = "4001 South 700 East"    

    def __init__(self, id):
        # Creating holders for all information needed
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

    # Gets all address and distance data into arrays to be searched
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
     
    # Gets the distance between two addresses
    def distanceBetween(self, address1, address2):
        # Return the float on the distance_data chart based on the two addresses
        return self.distance_data[self.address_list.index(address1)][self.address_list.index(address2)]

    # Loads the packages onto the truck in order
    def loadPackages(self, hash, lst):
        # Sort the packages using the greedy algorithm
        ordered_list = self.buildRoute(hash, lst)

        # Add all the packages to the trucks load and set the package status
        for package in ordered_list: 
            package.loaded_timestamp = self.current_time
            package.status = "En route"
            package.onTruck = self.id
            self.load.append(package.getId())

    # Finds the best route using greedy algorithm
    def buildRoute(self, hash, lst):
        # Create some temporary data holders
        temp_address = None
        nearest_pkg = None
        nearest_pkg_dist = 99.9
        ordered_list = []
        adj_list = list(lst)
        first_pkg = 0

        # Finding the package closest to the hub
        for package_id in lst:
            package = hash.get(package_id)
            temp_dist = self.distanceBetween(package.address, self.current_address)
            # If the currently examined package is closer than any previous package
            # make the current package the new nearest package
            if temp_dist < nearest_pkg_dist:
                nearest_pkg = package
                nearest_pkg_dist = temp_dist
            # Set the nearest package as out first package and update current our comparison address for later
            first_pkg = nearest_pkg.getId()
            temp_address = nearest_pkg.address
        # Add the first package to the sorted list and remove it from being compared again
        ordered_list.append(nearest_pkg)
        try:
            adj_list.remove(int(first_pkg))
        except:
            del first_pkg
        
        nearest_pkg = None

        # Sort through all other packages, using the greedy algorithm
        for p in lst:
            nearest_pkg_dist = 99.9
            try:
                for package_id in adj_list:
                    # Get the current package's distance from our comparison address
                    new_package = hash.get(package_id)
                    new_pkg_dist = self.distanceBetween(new_package.address, temp_address)

                    # If it's closer, update the new package to be the nearest package 
                    if new_pkg_dist < nearest_pkg_dist:
                        nearest_pkg = new_package
                        nearest_pkg_dist = new_pkg_dist
                
                # Add the package to the sorted list and remove it from being compared again
                ordered_list.append(nearest_pkg)
                adj_list.remove(nearest_pkg.getId())

                # Update the comparison address
                temp_address = nearest_pkg.address
            except:
                #adj_list is empty
                del nearest_pkg_dist

        # The last item always comes up None, so remove it from the sorted list
        ordered_list.pop()

        return ordered_list
    
    # Delivers the packages, sets their status, returns to the hub
    def deliverPackages(self, hash):
        # Iterate through all package in the current load
        for package_id in self.load:
            package = hash.get(package_id)

            # Update the mileage and time
            temp_dist = self.distanceBetween(self.current_address, package.address)
            self.mileage += temp_dist
            self.current_time += timedelta(minutes=(temp_dist / self.CONST_SPEED * 60))
            self.delivery_timestamps.append([self.mileage, self.current_time])

            # Deliver the package
            package.status = "Delivered"
            package.delivered_timestamp = self.current_time

            # Update the current address
            self.current_address = package.address
        # Clear out the load list
        self.load.clear()
        
        # Return to the hub
        dist_from_hub = self.distanceBetween(self.current_address, self.CONST_HUB_ADDRESS)
        self.current_time += timedelta(minutes=(dist_from_hub / self.CONST_SPEED * 60))
        self.delivery_timestamps.append([self.mileage, self.current_time])