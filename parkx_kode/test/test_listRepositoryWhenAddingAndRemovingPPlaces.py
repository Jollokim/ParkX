from unittest.mock import Mock

import pytest

from parkx_kode.repository.ListRepository import ListRepository

from parkx_kode.model.Parkingplace import Parkingplace



@pytest.fixture(scope="class")
def fakeRepo():
    repo = ListRepository()
    return repo


@pytest.fixture(scope="class")
def testParkingPlace():
    newTestParkingPlace = Parkingplace(1, "test1", "testAdress1", "testCode1", 15, 150, "test1.png", "placeholder1")
    return newTestParkingPlace


class Test_listRepository:

    def test_createsListRepository(self, fakeRepo):
        assert len(fakeRepo.getAllParkingPlaces()) == 0

    def test_addsNewParkingPlaceCorrectly(self, fakeRepo, testParkingPlace):
        fakeRepo.addNewParkingPlace(testParkingPlace)
        listOfParkingPlaces = fakeRepo.getAllParkingPlaces()
        assert listOfParkingPlaces[0] == testParkingPlace

    def test_removesAParkingPlaceCorrectly(self, fakeRepo, testParkingPlace):
        fakeRepo.removeParkingPlace(testParkingPlace)
        assert len(fakeRepo.getAllParkingPlaces()) == 0
