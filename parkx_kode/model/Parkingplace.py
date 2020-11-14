import datetime


class Parkingplace:
    def __init__(self, id, name, address, zip_code, number_of_places,
                 price_pr_hour, picture, details, available=True, parkingStarted=None):
        self.id = id
        self.name = name
        self.address = address
        self.zip_code = zip_code
        self.number_of_places = int(number_of_places)
        self.price_pr_hour = int(price_pr_hour)
        self.picture = picture
        self.details = details
        self.available = available
        self.parkingStarted = parkingStarted

    def toString(self):
        return str(f"ID: {self.id} Name: {self.name} Address: {self.address}"
                   f" PostAdr: {self.zip_code} Antall: {self.number_of_places}"
                   f"Pris: {self.price_pr_hour} Bilde: {self.picture}"
                   f"Detaljer: {self.details} Ledig: {self.available}")

    def toListNameToDetails(self):
        return [self.name, self.address, self.zip_code, self.number_of_places, self.price_pr_hour, self.picture,
                self.details]

    def updateAttributes(self, id, name, address, zip_code, number_of_places, price_pr_hour, picture, details):
        self.id = id
        self.name = name
        self.address = address
        self.zip_code = zip_code
        self.number_of_places = int(number_of_places)
        self.price_pr_hour = int(price_pr_hour)
        self.picture = picture
        self.details = details

    def updateParkingPlaceStatus(self):
        if self.available:
            self.available = False
            self.parkingStarted = datetime.datetime.now().strftime("%H:%M:%S")
        else:
            self.available = True

    def calculatePriceForParkingPeriod(self, parkingStopped):
        FMT = '%H:%M:%S'
        parkedTimeDelta = datetime.datetime.strptime(parkingStopped, FMT) \
                          - datetime.datetime.strptime(self.parkingStarted, FMT)

        ParkedTimeSec = parkedTimeDelta.total_seconds()
        ParkedTimeHour = (ParkedTimeSec / 3600)

        totalPrice = ParkedTimeHour * self.price_pr_hour
        totalPriceTwoDec = str("{:.2f}".format(totalPrice))
        return totalPriceTwoDec
