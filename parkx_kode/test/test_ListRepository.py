import pytest

from parkx_kode.repository.ListRepository import ListRepository



@pytest.fixture
def p_dict1():
    dict = {
        "id": 1,
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
def p_dict2():
    dict = {
        "id": 2,
        "name": "kalle balle",
        "address": "Kalle balle veien 5",
        "zip_code": 2013,
        "number_of_places": 2,
        "price_pr_hour": 25,
        "picture": "adresse.com",
        "details": "Dårlig utsikt men nær sentrum!"
    }
    return dict

@pytest.fixture
def p_dict3():
    dict = {
        "id": 3,
        "name": "Karbos",
        "address": "Karbos parkeringsplass",
        "zip_code": 3036,
        "number_of_places": 30,
        "price_pr_hour": 25,
        "picture": "adresse.com",
        "details": "Lei og finn en ledig plass"
    }
    return dict

@pytest.fixture
def repository(p_dict1, p_dict2, p_dict3):
    repo = ListRepository()

    repo.addNewParkingPlace(**p_dict1)
    repo.addNewParkingPlace(**p_dict2)
    repo.addNewParkingPlace(**p_dict3)

    return repo

def test_can_remove_from_ID(repository):
    repository.removeParkingPlace(2)

    assert len(repository.parkingPlaces) == 2

    object_removed = True

    for pp in repository.parkingPlaces:
        if pp.id == 2:
            object_removed = False

    assert object_removed


def test_can_get_parkingplace_from_ID(repository):
    pp = repository.getPP(2)

    assert pp.id == 2
