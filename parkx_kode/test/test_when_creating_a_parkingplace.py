import pytest

from controller.ParkingController import *


class TestParkingPlace:

    def test_CreatesParkingControllerProperly(self):
        pController = ParkingController("gui", "repository")
        assert pController.toString() == "Gui: gui Repository: repository"
        pytest.fail("No implementation in ParkingController yet, TBD")

    def test_ThatCounterWorks(self):
        pController = ParkingController("gui", "repository")
        assert pController.counter == 0
        pController.increaseCounter()
        assert pController.counter == 1

    def test_ParkingPlaceAddFunctionCalledCorrectly(self, mocker):
        pController = ParkingController("gui", "repository")
        spy = mocker.spy(pController, 'addNewParkingPlace')
        pController.addNewParkingPlace(5, "test", "test123", "1522", 5, 120, "url", "Light")
        assert spy.called
        pytest.fail("Error: the methode: addNewParkingPlace seems to have no implementation or is not called in "
                    "ParkingController")

    def test_ParkingPlaceRemoveFunctionCalledCorrectly(self, mocker):
        pController = ParkingController("gui", "repository")
        spy = mocker.spy(pController, 'deleteParkingPlace')
        pController.deleteParkingPlace("test123")
        assert spy.called
        pytest.fail("Error: the methode: deleteParkingPlace seems to have no implementation or is not called in "
                    "ParkingController")

    def test_ParkingPlaceGetAllExistingFunctionCalledCorrectly(self, mocker):
        pController = ParkingController("gui", "repository")
        spy = mocker.spy(pController, 'getAllExistingParkingPlaces')
        pController.getAllExistingParkingPlaces()
        assert spy.called
        pytest.fail("Error: the methode: getAllExistingParkingPlaces seems to have no implementation or is not called "
                    "in ParkingController")

    def test_ParkingPlaceGetAExistingFunctionCalledCorrectly(self, mocker):
        pController = ParkingController("gui", "repository")
        spy = mocker.spy(pController, 'getAExistingParkingPlace')
        pController.getAnExistingParkingPlace("test123")
        assert spy.called
        pytest.fail("Error: the methode: getAExistingParkingPlace seems to have no implementation or is not called "
                    "in ParkingController")