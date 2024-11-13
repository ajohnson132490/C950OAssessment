# Austin Johnson: WGU ID 009925209

# Import all files
import csv
from Hash import Hash
from Package import Package
from Truck import Truck
from datetime import datetime, timedelta

def truckLoads(truck):

    

def main():
    hash = Hash()

    with open('Resources/packages.csv') as package_file:
        reader = csv.reader(package_file, delimiter = ",")

        # Get every row in the csv file 
        for row in reader:
            # Create a new package based on the data in the row
            package = Package(int(row[0]), row[1], row[2], row[3], row[4],
                              row[5], row[6], row[7])
            
            # Insert into the hashtable
            hash.insertItem(package)

    truck1_first_load = [40, 37, 34, 31, 30, 29, 39, 35, 33, 26, 24, 23, 22, 21, 17, 12]
    truck2_first_load = [3, 18, 36, 38, 13, 15, 19, 16, 14, 20, 1, 2, 4, 5, 7, 8]

if __name__ == "__main__":
    main()