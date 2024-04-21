class Location:
    def __init__(self, name, longitude, latitude, region, country):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.region = region
        self.country = country
        self.history = []

    def add_history(self, history_entry):
        self.history.append(history_entry)
