import pytest

from model.parkingplace import *


class Test_parkingplace_class:

    def test_parameters_are_used_in_constructor_correct_id(self):
        pplace = parkingplace("0001", "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
        expected = "0001"
        actual = pplace.id
        assert actual == expected
        pytest.fail("An Error occurred: Id")

    def test_parameters_are_used_in_constructor_correct_name(self):
        pplace = parkingplace("0001", "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
        expected = "TestPlass"
        actual = pplace.name
        assert actual == expected
        pytest.fail("An Error occurred: name")

    def test_parameters_are_used_in_constructor_correct_address(self):
        pplace = parkingplace("0001", "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
        expected = "Adresseveien1"
        actual = pplace.address
        assert actual == expected
        pytest.fail("An Error occurred: address")

    def test_parameters_are_used_in_constructor_correct_zipcode(self):
        pplace = parkingplace("0001", "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
        expected = "1234"
        actual = pplace.zip_code
        assert actual == expected
        pytest.fail("An Error occurred: zipcode")

    def test_parameters_are_used_in_constructor_correct_number_of_spaces(self):
        pplace = parkingplace("0001", "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
        expected = "1"
        actual = pplace.number_of_places
        assert actual == expected
        pytest.fail("An Error occurred: number of spaces")


    def test_parameters_are_used_in_constructur_correct_price(self):
        pplace = parkingplace("0001", "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
        expected = "50"
        actual = pplace.price_pr_hour
        assert actual == expected
        pytest.fail("An Error occurred: price")

    def test_parameters_are_used_in_constructur_correct_picture(self):
        pplace = parkingplace("0001", "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
        expected = "NULL"
        actual = pplace.picture
        assert actual == expected
        pytest.fail("An Error occurred: picture")

    def test_parameters_are_used_in_constructur_correct_details(self):
        pplace = parkingplace("0001", "TestPlass", "Adresseveien1", "1234", "1", "50", "NULL", "Har lader")
        expected = "Har lader"
        actual = pplace.details
        assert actual == expected
        pytest.fail("An Error occurred:  details")

