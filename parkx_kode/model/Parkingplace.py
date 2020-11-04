import datetime


class Parkingplace:
    def __init__(self, id, name, address, zip_code, number_of_places, price_pr_hour, picture, details):
        self.id = id
        self.name = name
        self.address = address
        self.zip_code = zip_code
        self.number_of_places = int(number_of_places)
        self.price_pr_hour = int(price_pr_hour)
        self.picture = picture
        self.details = details
        self.available = True
        # self.parkingStarted = datetime.datetime.now().strftime("%H:%M:%S")
        self.parkingStarted = None

    def toString(self):
        return str(f"ID: {self.id} Name: {self.name} Address: {self.address}"
                   f" PostAdr: {self.zip_code} Antall: {self.number_of_places}"
                   f"Pris: {self.price_pr_hour} Bilde: {self.picture}"
                   f"Detaljer: {self.details} Ledig: {self.available}")



