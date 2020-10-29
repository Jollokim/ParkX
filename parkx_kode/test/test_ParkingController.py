import pytest
from mock import Mock
from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.repository.ListRepository import ListRepository

from parkx_kode.test.test_ListRepository import repository, p_dict1, p_dict2, p_dict3
# TODO: teste en ikke happy path

@pytest.fixture
def p_dict():
    dict = {
        "Navn": "abekatt",
        "Adresse": "olebole veien",
        "PostAdr": 1712,
        "Antall": 1,
        "Pris": 20,
        "Bilde": "adresse.com",
        "Detaljer": "Fin utsikt blandt flere ting!"
    }
    return dict


@pytest.fixture
def mock_repo():
    return Mock(spec=ListRepository)


@pytest.fixture
def controller_with_mock(mock_repo):
    controller = ParkingController(None, mock_repo)
    return controller


@pytest.fixture
def controller(repository):
    return ParkingController(None, repository)


def test_can_call_add_new_parking_place_with_dict(controller_with_mock, mock_repo, p_dict):
    controller_with_mock.add_parking_place_to_repo(p_dict)

    mock_repo.addNewParkingPlace.assert_called_with(p_dict)


def test_can_call_remove_parkingplace_from_id(controller_with_mock, mock_repo):
    controller_with_mock.remove_parkingplace(2)

    mock_repo.removeParkingPlace.assert_called_with(2)


def test_can_get_parkingplace_from_id(controller):
    pp = controller.get_pp_from_repo(2)

    assert pp.id == 2


def test_increaseCounter_increases_counter(controller_with_mock):
    controller_with_mock.increaseCounter()

    assert controller_with_mock.counter == 1
