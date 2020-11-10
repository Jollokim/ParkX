import pytest
from mock import Mock
from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.model.Parkingplace import Parkingplace
from parkx_kode.repository.ListRepository import ListRepository
from parkx_kode.test.test_ListRepository import repository, p_dict1, p_dict2, p_dict3

# TODO: teste en ikke happy path
# TODO: Fjerne tester fra parkingcontroller, controller testes i integrasjonstester
"""
@pytest.fixture
def p_dict():
    dict = {
        "name": "abekatt",
        "address": "olebole veien",
        "zip_code": 1712,
        "number_of_places": 1,
        "price_pr_hour": 20,
        "picture": "adresse.com",
        "details": "Fin utsikt blandt flere ting!"
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

    mock_repo.addNewParkingPlace.assert_called_with(**p_dict)


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
                                 "id": 2,
                                 "name": "kalle balle",
                                 "address": "Kalle balle veien 5",
                                 "zip_code": 2013,
                                 "number_of_places": 2,
                                 "price_pr_hour": 25,
                                 "picture": "adresse.com",
                                 "details": "Dårlig utsikt men nær sentrum!"
                             }),
                             (3, {
                                 "id": 1,
                                 "name": "abekatt",
                                 "address": "olebole veien",
                                 "zip_code": 1712,
                                 "number_of_places": 1,
                                 "price_pr_hour": 20,
                                 "picture": "adresse.com",
                                 "details": "Fin utsikt blandt flere ting!"
                             }),
                             (2, {
                                 "id": 3,
                                 "name": "Karbos",
                                 "address": "Karbos parkeringsplass",
                                 "zip_code": 3036,
                                 "number_of_places": 30,
                                 "price_pr_hour": 25,
                                 "picture": "adresse.com",
                                 "details": "Lei og finn en ledig plass"
                             })
                         ]
                         )
def test_can_change_pp(controller, id, p_dict):
    controller.change_pp(id, p_dict)

    pp = controller.get_pp_from_repo(id)

    assert pp.id == id
    assert pp.name == p_dict["name"]
    assert pp.address == p_dict["address"]
    assert pp.zip_code == p_dict["zip_code"]
    assert pp.number_of_places == p_dict["number_of_places"]
    assert pp.price_pr_hour == p_dict["price_pr_hour"]
    assert pp.picture == p_dict["picture"]
    assert pp.details == p_dict["details"]


def test_increaseCounter_increases_counter(controller_with_mock):
    controller_with_mock.increaseCounter()

    assert controller_with_mock.counter == 5
"""