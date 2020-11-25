from datetime import datetime, date

import pytest
from mock import patch
from freezegun import freeze_time

from parkx_kode.model.Parkingplace import Parkingplace


@pytest.fixture
def fakeParkingPlace():
    pPlace = Parkingplace(1, "TestPlass", "Adresseveien1", "1234", 1, float(50), "NULL", "Har lader")
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
        expected = float(50)
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
                   "PostAdr: 1234 Antall: 1Pris: 50.0 Bilde: NULLDetaljer: Har lader Ledig: True"
        assert actual == expected

    def test_updatesParkingPlaceStatusCorrectly(self, fakeParkingPlace):
        isTrueByDefault = fakeParkingPlace.available
        assert isTrueByDefault

        fakeParkingPlace.updateParkingPlaceStatus()
        statusShouldNowBeFalse = fakeParkingPlace.available

        assert statusShouldNowBeFalse == False

        fakeParkingPlace.updateParkingPlaceStatus()
        statusShouldBeTrueAgain = fakeParkingPlace.available

        assert statusShouldBeTrueAgain

    def test_savesDateTimeNowInObject(self, fakeParkingPlace):
        freezer = freeze_time('2019-12-12 20:00:00')
        freezer.start()

        fakeParkingPlace.updateParkingPlaceStatus()

        freezer.stop()

        assert fakeParkingPlace.parkingStarted == "20:00:00"

    def test_calculatesParkingPlacePriceCorrectly(self, fakeParkingPlace):
        # freezer sets the time to 20-19-12-12 20 o'clock, used to
        # test the datetime.now() inside of updateParkingPlaceStatus()
        freezer = freeze_time('2019-12-12 20:00:00')
        freezer.start()

        fakeParkingPlace.updateParkingPlaceStatus()

        freezer.stop()
        expectedToPay = float(fakeParkingPlace.price_pr_hour)
        actualPrice = float(fakeParkingPlace.calculatePriceForParkingPeriod("21:00:00"))

        assert expectedToPay == actualPrice

    def test_can_update_own_attributes(self, fakeParkingPlace):
        id = 3
        name = "hollo bollo"
        address = "hollo veien 3A"
        zip_code = 1467
        number_of_places = 12
        price_per_hour = 20
        picture = "some beautyfull picture"
        details = "Nice view and low trafic"

        fakeParkingPlace.updateAttributes(id, name, address, zip_code, number_of_places, price_per_hour, picture, details)

        assert fakeParkingPlace.id == id
        assert fakeParkingPlace.name == name
        assert fakeParkingPlace.address == address
        assert fakeParkingPlace.zip_code == zip_code
        assert fakeParkingPlace.number_of_places == number_of_places
        assert fakeParkingPlace.price_pr_hour == price_per_hour
        assert fakeParkingPlace.picture == picture
        assert fakeParkingPlace.details == details

    def test_can_reset_parkingStarted_to_None(self, fakeParkingPlace):
        fakeParkingPlace.parkingStarted = "10:40:29"

        fakeParkingPlace.reset_parkingStarted()

        assert fakeParkingPlace.parkingStarted == None