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
    truck1_first_load = [14, 15, 16, 13, 20, 21, 35, 34, 40, 1, 27, 19]
    truck2_first_load = [24, 22, 18, 36]
    truck1_second_load = [29, 28, 39, 33, 23, 11, 12, 5, 7, 2, 4]
    truck2_second_load = [25, 26, 31, 32, 37, 38, 8, 30, 3, 10, 17, 6]   
    truck1_third_load = [9] 

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

    truck1.loadPackages(hash, truck1_third_load)

    truck1.deliverPackages(hash)

    # Run the user interface
    userInterface()

def userInterface():
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
                returnToUserInterface()
            case "2":
                packageReport()
                returnToUserInterface()
            case "3":
                mileageReport()
                returnToUserInterface()
            case "4":
                print("Exit")
                quit()
            case default:
                option = None
                print("Invalid input, please try again.")
            
def allPackagesReport():
    print("haha")
        
def packageReport():
    # Report welcome screen
    print("-----------------------------")
    print("  Individual Package Report  ")
    print("-----------------------------")

    # Getting the package info
    try:
        package_id = int(input("Please enter the package ID number: "))
        time = datetime.strptime(input("Please enter the time in the following format: H:M AM/PM "), "%I:%M %p")
        
    except:
        print("Invalid input")
        packageReport()

    package = hash.get(package_id)

    # Reformatting the time to remove the date
    time = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)

    # Printing status based on what timestamps are available
    if (package.delivered_timestamp <= time):
        print(f"Delivered at {package.delivered_timestamp}")
    elif (package.loaded_timestamp <= time):
        print(f"Loaded at {package.loaded_timestamp}")
    else:
        print("At the hub")

def mileageReport():
    # Report welcome screen
    print("-----------------------------")
    print("        Truck Mileage        ")
    print("-----------------------------")

    # Pulling the data from the trucks. Truck 3 is never used
    print(f"Truck {truck1.id} mileage: {truck1.mileage:.2f} miles")
    print(f"Truck {truck2.id} mileage: {truck2.mileage:.2f} miles")
    print("Truck 3 mileage: 0.00 miles")

def returnToUserInterface():
    print()
    inpt = None
    while inpt is None:
        inpt = input("Press Enter to return to the main menu. ")
    print()
    userInterface()

if __name__ == "__main__":
    main()