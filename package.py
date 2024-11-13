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
        self.loaded_timestamp = None
        self.delivered_timestamp = None

    def readyForDelivery(self):
        if "At the hub" in self.status: 

    def getId(self):
        return self.id
    
    def getStatus(self):
        return self.status
