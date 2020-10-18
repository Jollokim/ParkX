import pytest

from model.parkingplace import *

class TestParkingplace_Class:

    def test_parameters_are_used_in_constructur_correct(self):
        Pplace = model.parkingplace("01","TestPlass","NULL","NULL","1","50","NULL","Har lader")
        expected = "TestPlass"
        actual = model.parkingplace.name
        assert actual == expected

