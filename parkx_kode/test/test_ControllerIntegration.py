import pytest
from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.repository.ListRepository import ListRepository


class TestControllerIntegration:

    def test_returnsListFromRepositoryProperly(self, controller, repository):
        expected = 0
        actual = len(controller.get_all_pp_from_list())

        assert expected == actual and len(repository.parkingPlaces) == expected

        controller.repository.addPlaceholderPlaces()
        expectedAfterAddingPlaceHolders = 3
        actual = len(controller.get_all_pp_from_list())

        assert actual == expectedAfterAddingPlaceHolders and \
               len(repository.parkingPlaces) == expectedAfterAddingPlaceHolders

    def test_receivesDictionaryFromUserSavesItInRepositoryAndCreatesTheObjectProperly(self, p_dictFromUserInput,
                                                                                      controller):
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

    def test_receivesIdFromUserAndDeletesCorrectParkingPlaceObject(self, controller, repositoryWithPlaceholders):
        controller.repository = repositoryWithPlaceholders
        #user id from UI
        id = 2

        objectStillInList = False
        for object in controller.get_all_pp_from_list():
            if object.id == id:
                objectStillInList = True

        assert objectStillInList

        controller.remove_parkingplace(id)

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


@pytest.fixture()
def repositoryWithPlaceholders():
    listRepo = ListRepository()
    listRepo.addPlaceholderPlaces()
    return listRepo
