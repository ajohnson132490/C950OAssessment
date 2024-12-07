class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes):
        # Creating holders for all information needed
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = "At the hub"
        self.loaded_timestamp = None
        self.onTruck = -1
        self.delivered_timestamp = None

    # Returns the id
    def getId(self):
        # return the package's ID number
        return self.id
