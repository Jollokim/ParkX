from core.main import *
from controller.ParkingController import *


class TestParkingPlace:

    def testCreatesParkingControllerProperly(self):
        pController = ParkingController("gui", "repository")
        assert pController.toString() == "Gui: gui Repository: repository"
