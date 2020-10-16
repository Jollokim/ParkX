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
        pytest.fail("No implementation in ParkingController yet, TBD")
