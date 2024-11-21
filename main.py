# Austin Johnson: WGU ID 009925209

# Import all files
import csv
from Hash import Hash
from Package import Package
from Truck import Truck
from datetime import datetime, timedelta

def main():
    hash = Hash()
    distance_data = [[0 for x in range(26)] for y in range(26)]
    address_list = []

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

    # Get all the distances in a 2d array
    with open('Resources/distances.csv') as distance_file:
        reader = csv.reader(distance_file, delimiter = ",")

        # Get every row in the csv file 
        row_index = 0
        for row in reader:
            for j in range(26):
                if row[j] != '':
                    # Put it in a table format
                    distance_data[row_index][j] = float(row[j])
                    distance_data[j][row_index] = float(row[j])
        row_index += 1

    # Get all the addresses in an array
    with open('Resources/addresses.csv') as address_file:
        reader = csv.reader(address_file, delimiter = ",")

        # Get every address in the csv file
        for address in reader:
            full_address = address[0].split("\n")
            street_address = full_address[1].strip()
            address_list.append(street_address)
            

    truck1_first_load = [40, 37, 34, 31, 30, 29, 39, 35, 33, 26, 24, 23, 22, 21, 17, 12]
    truck2_first_load = [3, 18, 36, 38, 13, 15, 19, 16, 14, 20, 1, 2, 4, 5, 7, 8]
    truck1_second_load = [6, 25]
    truck2_second_load = [9, 10, 11, 28, 32]

if __name__ == "__main__":
    main()