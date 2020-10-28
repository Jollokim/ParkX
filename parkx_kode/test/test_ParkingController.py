import pytest
from mock import Mock
from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.repository.ListRepository import ListRepository


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
def controller(mock_repo):
    controller = ParkingController(None, mock_repo)
    return controller


def test_can_add_new_parking_place_from_dict(controller, mock_repo, p_dict):
    controller.add_parking_place_to_repo(p_dict)

    mock_repo.addNewParkingPlace.assert_called_with(p_dict)


def test_increaseCounter_increases_counter(controller):
    controller.increaseCounter()

    assert controller.counter == 1
