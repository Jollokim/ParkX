import pytest
from freezegun import freeze_time
from mock import Mock

from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.model import Parkingplace
from parkx_kode.model.Payment import Payment
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

        assert controller.get_all_pp_from_list() == repository.parkingPlaces

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

    def test_controllerGetsSpecificParkingPlaceWithId(self, controller):
        controller.repository.addPlaceholderPlaces()
        id = 2
        returnedObjectFromRepo = controller.get_pp_from_repo(id)

        assert returnedObjectFromRepo.id == id

    def test_controllerChangesParkingPlaceAttributesProperly(self, controller, p_dictFromUserInput):
        controller.repository.addPlaceholderPlaces()

        # simulates the user sending new schema to modify his parkingplace offer
        # Here we will change the current object with id = 2 to our fixture dict that simulates user input
        controller.change_pp(p_dictFromUserInput, 2)

        changedObject = controller.get_pp_from_repo(2)
        changedObjectDict = changedObject.__dict__

        for dictKey in p_dictFromUserInput.keys():
            assert changedObjectDict.get(dictKey) == p_dictFromUserInput.get(dictKey)

    def test_controllerSendsRequestToChangeParkingPlaceStatusAndSavesStartDateCorrectly(self, controller):
        # sets the time to 12/12/2020 20 o'clock
        freezer = freeze_time('2019-12-12 20:00:00')
        freezer.start()

        controller.repository.addPlaceholderPlaces()
        # argument is parkingplace id

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

    def test_controllerReturnsCalculatedPriceForParkingBasedOnTimePassedSinceParkingStartCorrectly(self, controller):
        controller.repository.addPlaceholderPlaces()
        id = 2
        testingObject = controller.get_pp_from_repo(id)

        testingObject.parkingStarted = "20:00:00"

        calculatedPrice = controller.calc_parking_price(id, "21:00:00")
        calculatedPrice = float(calculatedPrice)
        expectedPrice = testingObject.price_pr_hour
        assert calculatedPrice == expectedPrice

    def test_controllerRaisesValueExceptionIfInputFieldsWhereIntExpectedIncludesLetters(self, controller,
                                                                                        p_dictFromUserInputUnhappyPathLetter):
        with pytest.raises(ValueError):
            controller.add_parking_place_to_repo(p_dictFromUserInputUnhappyPathLetter)

        controller.repository.addPlaceholderPlaces()
        with pytest.raises(ValueError):
            controller.change_pp(p_dictFromUserInputUnhappyPathLetter, 2)

    def test_controllerRaisesUserWarningIfInputFieldIsEmpty(self, controller, p_dictFromUserInputUnhappyPathEmpty):
        with pytest.raises(UserWarning):
            controller.add_parking_place_to_repo(p_dictFromUserInputUnhappyPathEmpty)

        controller.repository.addPlaceholderPlaces()
        with pytest.raises(UserWarning):
            controller.change_pp(p_dictFromUserInputUnhappyPathEmpty, 2)

    def test_can_reset_parking_started(self, controller):
        controller.repository.addPlaceholderPlaces()

        controller.repository.parkingPlaces[0].parkingStarted = "12:12:43"

        controller.reset_parking_started(0)

        assert controller.repository.parkingPlaces[0].parkingStarted == None

    def test_can_add_new_payment_to_ListRepository(self, controller, payment_dict):
        controller.add_new_payment(
            payment_dict["name"], payment_dict["parkingStarted"], payment_dict["parkingStopped"], payment_dict["price"]
        )

        assert len(controller.repository.payments) == 1

        assert controller.repository.payments[0]["name"] == payment_dict["name"]
        assert controller.repository.payments[0]["parkingStarted"] == payment_dict["parkingStarted"]
        assert controller.repository.payments[0]["parkingStopped"] == payment_dict["parkingStopped"]
        assert controller.repository.payments[0]["price"] == payment_dict["price"]

    def test_can_get_list_with_all_payments(self, controller, payment_dict):
        # add some payments to the list
        for i in range(3):
            controller.add_new_payment(
                payment_dict["name"], payment_dict["parkingStarted"], payment_dict["parkingStopped"],
                payment_dict["price"]
            )

        list_of_payments = controller.get_all_payments()

        assert isinstance(list_of_payments, list)
        assert len(list_of_payments) == 3

        assert list_of_payments[0]["name"] == payment_dict["name"]
        assert list_of_payments[0]["parkingStarted"] == payment_dict["parkingStarted"]
        assert list_of_payments[0]["parkingStopped"] == payment_dict["parkingStopped"]
        assert list_of_payments[0]["price"] == payment_dict["price"]

    def test_can_empty_all_payments_from_list_if_acceptedPaymentDetails_is_true(self, controller, payment_dict):
        # add some payments to the list
        for i in range(3):
            controller.add_new_payment(
                payment_dict["name"], payment_dict["parkingStarted"], payment_dict["parkingStopped"],
                payment_dict["price"]
            )
        controller.payment.acceptedPaymentDetails = True

        controller.pay_all_payments()

        assert len(controller.repository.payments) == 0

    def test_can_not_empty_all_payments_from_list_if_acceptedPaymentDetails_is_false(self, controller, payment_dict):
        # add some payments to the list
        for i in range(3):
            controller.add_new_payment(
                payment_dict["name"], payment_dict["parkingStarted"], payment_dict["parkingStopped"],
                payment_dict["price"]
            )
        controller.payment.acceptedPaymentDetails = False

        controller.pay_all_payments()

        assert len(controller.repository.payments) == 3

    def test_can_change_accepted_payment_details(self, controller):
        controller.payment.acceptedPaymentDetails = False

        controller.change_accepted_payment_details(True)

        assert controller.payment.acceptedPaymentDetails == True

        controller.change_accepted_payment_details(False)

        assert controller.payment.acceptedPaymentDetails == False

    def test_can_get_accepted_payment_details_state_from_Payment(self, controller):
        controller.payment.acceptedPaymentDetails = True

        assert controller.check_accepted_payment_details() == controller.payment.acceptedPaymentDetails


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
def p_dictFromUserInputUnhappyPathLetter():
    dict = {
        "name": "abekatt",
        "address": "olebole veien",
        "zip_code": "1712",
        "number_of_places": "1s",
        "price_pr_hour": "20",
        "picture": "adresse.com",
        "details": "Fin utsikt blandt flere ting!"
    }
    return dict


@pytest.fixture
def p_dictFromUserInputUnhappyPathEmpty():
    dict = {
        "name": "abekatt",
        "address": "olebole veien",
        "zip_code": "1712",
        "number_of_places": "",
        "price_pr_hour": "20",
        "picture": "adresse.com",
        "details": "Fin utsikt blandt flere ting!"
    }
    return dict


@pytest.fixture
def payment_dict():
    payment = {
        "name": "KarlsByGaten",
        "parkingStarted": "11:12:13",
        "parkingStopped": "11:30:57",
        "price": 30
    }
    return payment


@pytest.fixture
def repository():
    return ListRepository()


@pytest.fixture
def payment(repository):
    return Payment(repository)


@pytest.fixture
def controller(payment, repository):
    return ParkingController(None, payment, repository)

# brukes ikke og kan fjernes
# @pytest.fixture
# def mock_ListRepository():
#     mock = Mock(spec=ListRepository)
#     mock.parkingPlaces = []
#     return mock
#
#
# @pytest.fixture
# def mock_Payment():
#     return Mock(spec=Payment)
#
#
# @pytest.fixture
# def mock_Parkingplace():
#     mock = Mock(spec=Parkingplace)
#
#     return mock
#
#
# @pytest.fixture
# def controller_with_mock(mock_Payment, mock_ListRepository):
#     return ParkingController(None, mock_Payment, mock_ListRepository)
