import pytest
from freezegun import freeze_time

from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.repository.ListRepository import ListRepository


class TestControllerIntegration:

    #Implements ParkX.Leie-plassen.01
    def test_returnsListFromRepositoryProperly(self, controller, repository):
        expected = 0
        actual = len(controller.get_all_pp_from_list())

        assert expected == actual and len(repository.parkingPlaces) == expected

        controller.repository.addPlaceholderPlaces()
        expectedAfterAddingPlaceHolders = 3
        actual = len(controller.get_all_pp_from_list())

        assert actual == expectedAfterAddingPlaceHolders and \
               len(repository.parkingPlaces) == expectedAfterAddingPlaceHolders

        assert controller.get_all_pp_from_list() == repository.parkingPlaces

    #Implements ParkX.Utleie-plaseen.01
    def test_receivesDictionaryFromUserSavesItInRepositoryAndCreatesTheObjectProperly(self, p_dictFromUserInput, controller):
        lengthBeforeAddCall = len(controller.repository.parkingPlaces)
        controller.add_parking_place_to_repo(p_dictFromUserInput)

        # mockedRepoController = ParkingController(None, mock_repo)
        # mockedRepoController.add_parking_place_to_repo(p_dictFromUserInput)
        # mock_repo.addNwassert_called_with(**p_dictFromUserInput)

        assert len(controller.repository.parkingPlaces) == (lengthBeforeAddCall + 1)

        savedObject = controller.repository.getAllParkingPlaces()[0]

        savedObjectDict = savedObject.__dict__

        for dictKey in p_dictFromUserInput.keys():
            assert p_dictFromUserInput.get(dictKey) == savedObjectDict.get(dictKey)

    def test_increaseCounter_increases_counter(self, controller):
        controller.increaseCounter()

        assert controller.counter == 5

    #Implements ParkX.Utleie-plassen.02.01
    def test_receivesIdFromUserAndDeletesCorrectParkingPlaceObject(self, controller):
        controller.repository.addPlaceholderPlaces()
        listLength = len(controller.get_all_pp_from_list())
        assert listLength == 3

        # user id from UI
        id = 2

        objectStillInList = False
        for object in controller.get_all_pp_from_list():
            if object.id == id:
                objectStillInList = True

        assert objectStillInList

        controller.remove_parkingplace(id)

        objectStillInList = False

        for object in controller.get_all_pp_from_list():
            if object.id == id:
                objectStillInList = True

        assert objectStillInList == False

        listLength = len(controller.get_all_pp_from_list())
        assert listLength == 2

    #Implements ParkX.leie-plassen.07
    def test_controllerGetsSpecificParkingPlaceWithId(self, controller):
        controller.repository.addPlaceholderPlaces()
        id = 2
        returnedObjectFromRepo = controller.get_pp_from_repo(id)

        assert returnedObjectFromRepo.id == id

    #Implements ParkX.utleie-plassen.03
    def test_controllerChangesParkingPlaceAttributesProperly(self, controller, p_dictFromUserInput):
        controller.repository.addPlaceholderPlaces()

        #simulates the user sending new schema to modify his parkingplace offer
        #Here we will change the current object with id = 2 to our fixture dict that simulates user input
        controller.change_pp(p_dictFromUserInput, 2)

        changedObject = controller.get_pp_from_repo(2)
        changedObjectDict = changedObject.__dict__

        for dictKey in p_dictFromUserInput.keys():
            assert changedObjectDict.get(dictKey) == p_dictFromUserInput.get(dictKey)

    #Implements ParkX.Leie-plassen.01 + ParkX.Leie-plassen.05
    def test_controllerSendsRequestToChangeParkingPlaceStatusAndSavesStartDateCorrectly(self, controller):
        #sets the time to 12/12/2020 20 o'clock
        freezer = freeze_time('2019-12-12 20:00:00')
        freezer.start()

        controller.repository.addPlaceholderPlaces()
        #argument is parkingplace id

        changedObject = controller.get_pp_from_repo(2)
        beforeUpdateExpectedFalse = True
        defaultParkingStartedValue = None

        assert changedObject.available == beforeUpdateExpectedFalse
        assert changedObject.parkingStarted == defaultParkingStartedValue

        controller.change_pp_status(2)

        expectedFalseAfterUpdate = False
        expectedParkingStartedValueAfterUpdate = "20:00:00"

        assert changedObject.available == expectedFalseAfterUpdate
        assert changedObject.parkingStarted == expectedParkingStartedValueAfterUpdate

        freezer.stop()

    #Implements ParkX.Leie-plassen.05
    def test_controllerReturnsCalculatedPriceForParkingBasedOnTimePassedSinceParkingStartCorrectly(self, controller):
        controller.repository.addPlaceholderPlaces()
        id = 2
        testingObject = controller.get_pp_from_repo(id)

        testingObject.parkingStarted = "20:00:00"

        calculatedPrice = controller.calc_parking_price(id, "21:00:00")
        calculatedPrice = float(calculatedPrice)
        expectedPrice = testingObject.price_pr_hour
        assert calculatedPrice == expectedPrice


# TODO: teste en ikke happy path


@pytest.fixture
def p_dictFromUserInput():
    dict = {
        "name": "abekatt",
        "address": "olebole veien",
        "zip_code": "1712",
        "number_of_places": "1",
        "price_pr_hour": "20",
        "picture": "adresse.com",
        "details": "Fin utsikt blandt flere ting!"
    }
    return dict


@pytest.fixture
def repository():
    return ListRepository()


@pytest.fixture
def controller(repository):
    return ParkingController(None, repository)
