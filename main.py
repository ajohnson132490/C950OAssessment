# Austin Johnson: WGU ID 009925209

# Import all files
import csv
from Hash import Hash
from Package import Package
from Truck import Truck
from datetime import datetime, timedelta

# Create the hashtable
hash = Hash()

# Create the trucks
truck1 = Truck(1)
truck2 = Truck(2)

def main():
    # Get all the packages in the hash
    with open('Resources/packages.csv') as package_file:
        reader = csv.reader(package_file, delimiter = ",")

        # Get every row in the csv file 
        for row in reader:
            # Create a new package based on the data in the row
            package = Package(int(row[0]), row[1], row[2], row[3], row[4],
                              row[5], row[6], row[7])
            
            if (package.getId() == 9):
                package.address = "410 S State St"
                package.city = "Salt Lake City"
                package.state = "UT"
                package.zip = "84111"

            # Insert into the hashtable
            hash.insertItem(package)
            

    # Creating out loads to maximize efficiency
    truck1_first_load = [40, 37, 34, 31, 30, 29, 39, 35, 33, 26, 24, 23, 22, 21, 17, 12]
    truck2_first_load = [3, 18, 36, 38, 13, 15, 19, 16, 14, 20, 1, 2, 4, 5, 7, 8]
    truck1_second_load = [6, 25, 11]
    truck2_second_load = [9, 10, 28, 32]

    # Load and deliver the first route
    truck1.loadPackages(hash, truck1_first_load)
    truck2.loadPackages(hash, truck2_first_load)

    truck1.deliverPackages(hash)
    truck2.deliverPackages(hash)

    # Load and deliver the second route
    truck1.loadPackages(hash, truck1_second_load)
    truck2.loadPackages(hash, truck2_second_load)

    truck1.deliverPackages(hash)
    truck2.deliverPackages(hash)

    #print(truck1.delivery_timestamps)
    #print(str(truck1.delivery_timestamps[0][1]))

    userInterface(hash)

def userInterface(hash):
    # Welcome screen
    print("-----------------------------")
    print("      WGU Parcel Service     ")
    print("-----------------------------")

    # Menu options
    print("Please select one of the following options:")
    print("\t 1. Delivery Report By Time")
    print("\t 2. Delivery Report By Package")
    print("\t 3. Truck Mileage")
    print("\t 4. Exit")

    # Generate report by option
    option = None
    while option is None: 
        option = input()

        match option:
            case "1":
                allPackagesReport()
            case "2":
                packageReport()
            case "3":
                mileageReport()
            case "4":
                print("Exit")
                quit()
            case default:
                option = None
                print("Invalid input, please try again.")
            
def allPackagesReport():
    print("haha")
        
def packageReport():
    print("haha")

def mileageReport():
    # Report welcome screen
    print("-----------------------------")
    print("        Truck Mileage        ")
    print("-----------------------------")

    # Pulling the data from the trucks. Truck 3 is never used
    print(f"Truck {truck1.id} mileage: {truck1.mileage:.2f} miles")
    print(f"Truck {truck2.id} mileage: {truck2.mileage:.2f} miles")
    print("Truck 3 mileage: 0.00 miles")

if __name__ == "__main__":
    main()