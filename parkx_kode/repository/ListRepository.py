from parkx_kode.model.Parkingplace import Parkingplace


class ListRepository:
    def __init__(self):
        parking1 = Parkingplace("0001", "Første eksempel parkering","Parkeringsveien 1","1231","1","25", "shorturl.at/ruL57","Har lader og god belysning","yes")
        parking2 = Parkingplace("0002", "Andre eksempel parkering", "Parkeringsgata 81", "1001", "1", "95", "shorturl.at/ixAG5", "Har lader og god belysning. Innendørs","yes")
        parking3 = Parkingplace("0003", "Tredje eksempel parkering", "Kjøreveien 84", "1521", "1", "1", "shorturl.at/rOQUW", "Utendørs uten noe","no")
        parking4 = Parkingplace("0004", "Fjerde eksempel parkering", "Sykkelveien 254", "1539", "2", "15", "shorturl.at/iotP3", "En vegglampe","yes")
        self.parkingPlaces = [parking1,parking2,parking3,parking4]

    def getAllParkingPlaces(self):
        return self.parkingPlaces

    def addNewParkingPlace(self, p_dict):
        new_pp = Parkingplace(p_dict["ID"], p_dict["Navn"], p_dict["Adresse"], p_dict["PostAdr"], p_dict["Antall"],
                              p_dict["Pris"], p_dict["Bilde"], p_dict["Detaljer"], p_dict["Available"])

        self.parkingPlaces.append(new_pp)

    def removeParkingPlace(self, id):
        self.parkingPlaces.remove(self.getPP(id))

    def getPP(self, id):
        for pp in self.parkingPlaces:
            if pp.id == id:
                return pp

    def changePP(self, id, p_dict):
        pp = self.getPP(id)

        pp.name = p_dict["Name"]
        pp.address = p_dict["Adresse"]
        pp.zip_code = p_dict["PostAdr"]
        pp.number_of_place = p_dict["Antall"]
        pp.price_pr_hour = p_dict["Pris"]
        pp.picture = p_dict["Bilde"]
        pp.details = p_dict["Detaljer"]
        pp.available = p_dict["Available"]
