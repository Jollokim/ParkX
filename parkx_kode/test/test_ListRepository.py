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
        "Navn": "kalle balle",
        "Adresse": "Kalle balle veien 5",
        "PostAdr": 2013,
        "Antall": 2,
        "Pris": 25,
        "Bilde": "adresse.com",
        "Detaljer": "Dårlig utsikt men nær sentrum!"
    }
    return dict

@pytest.fixture
def p_dict3():
    dict = {
        "ID": 3,
        "Navn": "Karbos",
        "Adresse": "Karbos parkeringsplass",
        "PostAdr": 3036,
        "Antall": 30,
        "Pris": 25,
        "Bilde": "adresse.com",
        "Detaljer": "Lei og finn en ledig plass"
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


# @pytest.mark.parametrize("id, p_dict", [
#     (1, p_dict2),
#     (3, p_dict1),
#     (2, p_dict3)
# ])
# def test_can_change_a_parkingplace(repository, id, p_dict):
#     repository.changePP(id, p_dict)
#
#     pp = repository.get_pp_from_repo(id)
#
#     assert pp.id == id
#     assert pp.name == p_dict["Name"]
#     assert pp.address == p_dict["Adresse"]
#     assert pp.zip_code == p_dict["PostAdr"]
#     assert pp.number_of_place == p_dict["Antall"]
#     assert pp.price_pr_hour == p_dict["Pris"]
#     assert pp.picture == p_dict["Bilde"]
#     assert pp.details == p_dict["Detaljer"]