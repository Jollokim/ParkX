import pytest
from repository.ListRepository import ListRepository

from model.parkingplace import parkingplace


class Test_arrayRepository:
    Repo = ListRepository()
    newPPlace = parkingplace(1, "test1", "testAdress1", "testCode1", 15, 150, "test1.png", "placeholder1")

    def test_createsArrayRepository(self):
        assert len(Test_arrayRepository.Repo.getAllParkingPlaces()) == 0

    def test_addsNewParkingPlaceCorrectly(self):
        Test_arrayRepository.Repo.addNewParkingPlace(Test_arrayRepository.newPPlace)
        assert Test_arrayRepository.Repo.parkingPlaces[0] == Test_arrayRepository.newPPlace and len(Test_arrayRepository.Repo.parkingPlaces) == 1

    def test_removesAParkingPlaceCorrectly(self):
        Test_arrayRepository.Repo.removeParkingPlace(Test_arrayRepository.newPPlace)
        assert len(Test_arrayRepository.Repo.parkingPlaces) == 0