from datetime import datetime, timedelta

class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = "At the hub"

    def getAssociatedPackages(self, hashTable):
        # If this current package must be delivered with other packages
        if "Must" in self.notes:
            associated_packages = []

            # Get the package ID
            split_note = self.replace(",", " ").split()
            associated_ids = [int(i) for i in split_note if i.isdigit()]

            for package_id in associated_ids:
                package = hashTable.getPackage(package_id)
                associated_packages.append(package)
                #make it recursive

