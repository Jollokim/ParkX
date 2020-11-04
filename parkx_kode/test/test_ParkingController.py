import pytest
from mock import Mock
from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.model.Parkingplace import Parkingplace
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


def test_can_get_all_parkingplaces_in_list(controller):
    pp_list = controller.get_all_pp_from_list()

    assert isinstance(pp_list, list)

    if len(pp_list) > 0:
        assert isinstance(pp_list[0], Parkingplace)


@pytest.mark.parametrize("id, p_dict",
                         [
                             (1, {
                                 "ID": 2,
                                 "Navn": "kalle balle",
                                 "Adresse": "Kalle balle veien 5",
                                 "PostAdr": 2013,
                                 "Antall": 2,
                                 "Pris": 25,
                                 "Bilde": "adresse.com",
                                 "Detaljer": "Dårlig utsikt men nær sentrum!"
                             }),
                             (3, {
                                 "ID": 1,
                                 "Navn": "abekatt",
                                 "Adresse": "olebole veien",
                                 "PostAdr": 1712,
                                 "Antall": 1,
                                 "Pris": 20,
                                 "Bilde": "adresse.com",
                                 "Detaljer": "Fin utsikt blandt flere ting!"
                             }),
                             (2, {
                                 "ID": 3,
                                 "Navn": "Karbos",
                                 "Adresse": "Karbos parkeringsplass",
                                 "PostAdr": 3036,
                                 "Antall": 30,
                                 "Pris": 25,
                                 "Bilde": "adresse.com",
                                 "Detaljer": "Lei og finn en ledig plass"
                             })
                         ]
                         )
def test_can_change_pp(controller, id, p_dict):
    controller.change_pp(id, p_dict)

    pp = controller.get_pp_from_repo(id)

    assert pp.id == id
    assert pp.name == p_dict["Navn"]
    assert pp.address == p_dict["Adresse"]
    assert pp.zip_code == p_dict["PostAdr"]
    assert pp.number_of_places == p_dict["Antall"]
    assert pp.price_pr_hour == p_dict["Pris"]
    assert pp.picture == p_dict["Bilde"]
    assert pp.details == p_dict["Detaljer"]


def test_increaseCounter_increases_counter(controller_with_mock):
    controller_with_mock.increaseCounter()

    assert controller_with_mock.counter == 1
