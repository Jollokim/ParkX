import pytest

from controller.ParkingController import ParkingController


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
        pController.add_parking_place(None)
        assert spy.called
        pytest.fail("No implementation in ParkingController yet, TBD")
