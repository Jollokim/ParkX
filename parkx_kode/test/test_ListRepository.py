from parkx_kode.repository.ListRepository import ListRepository

import pytest


class TestListRepository:

    def test_getsAllParkingPlacesCorrectly(self, repository, parkingObject1, parkingObject2, parkingObject3):
        expectedParkingPlaceList = [parkingObject1, parkingObject2, parkingObject3]

        actualParkingPlaceList = repository.getAllParkingPlaces()

        for parkingPlaceId in range(len(actualParkingPlaceList)):
            if expectedParkingPlaceList[parkingPlaceId] != actualParkingPlaceList[parkingPlaceId]:
                pytest.fail(f"Parkingplaces do not match")

    def test_addsNewParkingPlaceCorrectly(self, p_dict1, repository):
        repository.addNewParkingPlace(**p_dict1)

        repoParkingPlaceDict = repository.getPP(p_dict1["id"]).__dict__

        assert repoParkingPlaceDict == p_dict1

    def test_can_remove_from_ID(self, repository):
        repository.removeParkingPlace(2)

        assert len(repository.parkingPlaces) == 2

        object_removed = True

        for pp in repository.parkingPlaces:
            if pp.id == 2:
                object_removed = False

        assert object_removed

    def test_can_get_parkingplace_from_ID(self, repository):
        pp = repository.getPP(2)

        assert pp.id == 2

    def test_changesParkingPlaceCorrectly(self, repository, p_dict2):
        p_dict2["id"] = 1

        repository.changePP(p_dict2)

        changedFirstInListParkingPlace = repository.getPP(1)

        assert changedFirstInListParkingPlace.__dict__ == p_dict2

    def test_createsPlaceHoldersCorrectly(self, emptyRepo):
        emptyRepo.addPlaceholderPlaces()
        placeHolderList = emptyRepo.getAllParkingPlaces()

        assert len(placeHolderList) == 3


@pytest.fixture
def emptyRepo():
    return ListRepository()


@pytest.fixture
def repository(p_dict1, p_dict2, p_dict3):
    repo = ListRepository()

    repo.addNewParkingPlace(**p_dict1)
    repo.addNewParkingPlace(**p_dict2)
    repo.addNewParkingPlace(**p_dict3)

    return repo


@pytest.fixture
def parkingObject1(repository):
    return repository.getPP(1)


@pytest.fixture
def parkingObject2(repository):
    return repository.getPP(2)


@pytest.fixture
def parkingObject3(repository):
    return repository.getPP(3)


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
        "details": "Fin utsikt blandt flere ting!",
        "available": True,
        "parkingStarted": None
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
        "details": "Dårlig utsikt men nær sentrum!",
        "available": True,
        "parkingStarted": None
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
        "details": "Lei og finn en ledig plass",
        "available": True,
        "parkingStarted": None
    }
    return dict
