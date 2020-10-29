import pytest

from parkx_kode.repository.ListRepository import ListRepository



@pytest.fixture
def p_dict1():
    dict = {
        "ID": 1,
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
def p_dict2():
    dict = {
        "ID": 2,
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
def p_dict3():
    dict = {
        "ID": 3,
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
def repository(p_dict1, p_dict2, p_dict3):
    repo = ListRepository()

    repo.addNewParkingPlace(p_dict1)
    repo.addNewParkingPlace(p_dict2)
    repo.addNewParkingPlace(p_dict3)

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