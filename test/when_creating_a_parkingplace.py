from core.main import *
from controller.ParkingController import *


class TestParkingPlace:

    def test_CreatesParkingControllerProperly(self):
        pController = ParkingController("gui", "repository")
        assert pController.toString() == "Gui: gui Repository: repository"

    def test_ThatCounterWorks(self):
        pController = ParkingController("gui", "repository")
        assert pController.getCounter() == 0
        pController.increaseCoutner()
        assert pController.getCounter() == 1

