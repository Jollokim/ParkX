from core.main import *
from controller.ParkingController import *


class TestParkingPlace:

    def __init__(self):
        self.pController = ParkingController("gui", "repository")

    def testCreatesParkingControllerProperly(self):
        assert self.pController.toString() == "Gui: gui Repository: repository"

    def testThatCounterWorks(self):
        assert 0
