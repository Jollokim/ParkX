import pytest

from parkx_kode.model.Parkingplace import Parkingplace


@pytest.fixture
def fakeParkingPlace():
    pPlace = Parkingplace(1, "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
    return pPlace


class Test_parkingplace_class:

    def test_parameters_are_used_in_constructor_correct_id(self, fakeParkingPlace):
        expected = 1
        actual = fakeParkingPlace.id
        assert actual == expected

    def test_parameters_are_used_in_constructor_correct_name(self, fakeParkingPlace):
        expected = "TestPlass"
        actual = fakeParkingPlace.name
        assert actual == expected

    def test_parameters_are_used_in_constructor_correct_address(self, fakeParkingPlace):
        expected = "Adresseveien1"
        actual = fakeParkingPlace.address
        assert actual == expected

    def test_parameters_are_used_in_constructor_correct_zipcode(self, fakeParkingPlace):
        expected = "1234"
        actual = fakeParkingPlace.zip_code
        assert actual == expected

    def test_parameters_are_used_in_constructor_correct_number_of_spaces(self, fakeParkingPlace):
        expected = 1
        actual = fakeParkingPlace.number_of_places
        assert actual == expected

    def test_parameters_are_used_in_constructor_correct_price(self, fakeParkingPlace):
        expected = 50
        actual = fakeParkingPlace.price_pr_hour
        assert actual == expected

    def test_parameters_are_used_in_constructor_correct_picture(self, fakeParkingPlace):
        expected = "NULL"
        actual = fakeParkingPlace.picture
        assert actual == expected

    def test_parameters_are_used_in_constructor_correct_details(self, fakeParkingPlace):
        expected = "Har lader"
        actual = fakeParkingPlace.details
        assert actual == expected

    def test_availibleAttributeTrueByDefault(self, fakeParkingPlace):
        expected = True
        actual = fakeParkingPlace.available
        assert actual == expected

    def test_parkingStartedAttributeNoneByDefault(self, fakeParkingPlace):
        expected = None
        actual = fakeParkingPlace.parkingStarted
        assert actual == expected

    def test_entireObjectCreatedProperly(self, fakeParkingPlace):
        actual = fakeParkingPlace.toString()
        expected = "ID: 1 Name: TestPlass Address: Adresseveien1 " \
                   "PostAdr: 1234 Antall: 1Pris: 50 Bilde: NULLDetaljer: Har lader Ledig: True"
        assert actual == expected
