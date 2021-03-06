from parkx_kode.model.Parkingplace import Parkingplace


class ListRepository:
    def __init__(self):
        self.parkingPlaces = []
        self.payments = []

    def getAllParkingPlaces(self):
        return self.parkingPlaces

    def addNewParkingPlace(self, id, name, address, zip_code, number_of_places,
                           price_pr_hour, picture, details, available=True, parkingStarted=None):

        new_pp = Parkingplace(id, name, address, zip_code, number_of_places,
                              price_pr_hour, picture, details, available, parkingStarted)

        self.parkingPlaces.append(new_pp)

    def removeParkingPlace(self, id):
        self.parkingPlaces.remove(self.getPP(id))

    def getPP(self, id):
        for pp in self.parkingPlaces:
            if pp.id == id:
                return pp

    def changePP(self, p_dict):
        parkingPlaceId = p_dict["id"]
        pp = self.getPP(parkingPlaceId)
        pp.updateAttributes(**p_dict)

    def updateParkingPlaceStatus(self, id):
        parkingPlaceObject = self.getPP(id)
        parkingPlaceObject.updateParkingPlaceStatus()

    def calculatePriceForParkingPeriod(self, id, parkingStopped):
        parkingPlaceObject = self.getPP(id)
        calculatedPrice = parkingPlaceObject.calculatePriceForParkingPeriod(parkingStopped)
        return calculatedPrice

    def addPlaceholderPlaces(self):
        pPlace1 = {
            "id": 0,
            "name": "Hjembua",
            "address": "Hjørneveien 3",
            "zip_code": 1882,
            "number_of_places": 1,
            "price_pr_hour": float(8234),
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Hjørneparkering med god plass. Lys i taket."
        }

        pPlace2 = {
            "id": 1,
            "name": "Parkveien",
            "address": "Parkveien 73A",
            "zip_code": 7123,
            "number_of_places": 1,
            "price_pr_hour": float(42),
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Har lys på veggen, og 1 stk 230V kontakt på plassen"
        }

        pPlace3 = {
            "id": 2,
            "name": "Storgata",
            "address": "Storgata 565",
            "zip_code": 1629,
            "number_of_places": 1,
            "price_pr_hour": float(89),
            "picture": "http://www.visafo.no/upload/services/oppmerking/parkeringsplass-ortustranda_borettslag_4.jpg",
            "details": "Ligger under bakken. Strøm på noen av plassene. Lys på alle plasser. Varmt og tørt."
        }

        self.addNewParkingPlace(**pPlace1)

        self.addNewParkingPlace(**pPlace2)

        self.addNewParkingPlace(**pPlace3)

    def add_payment(self, pay_dict):
        self.payments.append(pay_dict)

    def remove_all_payments(self):
        self.payments.clear()

    def get_all_payments(self):
        return self.payments
