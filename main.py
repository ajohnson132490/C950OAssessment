# Austin Johnson: WGU ID 009925209

# Import all files
import csv
from Hash import Hash
from package import Package
from truck import Truck
from datetime import datetime, timedelta

def main():
    hash = Hash()

    # Get all the packages in the hash
    with open('Resources/packages.csv') as package_file:
        reader = csv.reader(package_file, delimiter = ",")

        # Get every row in the csv file 
        for row in reader:
            # Create a new package based on the data in the row
            package = Package(int(row[0]), row[1], row[2], row[3], row[4],
                              row[5], row[6], row[7])
            
            # Insert into the hashtable
            hash.insertItem(package)
            

    # Creating out loads to maximize efficiency
    truck1_first_load = [40, 37, 34, 31, 30, 29, 39, 35, 33, 26, 24, 23, 22, 21, 17, 12]
    truck2_first_load = [3, 18, 36, 38, 13, 15, 19, 16, 14, 20, 1, 2, 4, 5, 7, 8]
    truck1_second_load = [6, 25]
    truck2_second_load = [9, 10, 11, 28, 32]

    # Create the trucks
    truck1 = Truck(1)
    truck2 = Truck(2)
    truck1.loadPackages(hash, truck1_first_load)
    truck2.loadPackages(hash, truck2_first_load)

if __name__ == "__main__":
    main()