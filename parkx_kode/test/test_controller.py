import pytest

from parkx_kode.controller.ParkingController import ParkingController
from parkx_kode.view.gui import Gui
from parkx_kode.model.parkingplace import Parkingplace




@pytest.mark.parametrize("p_data, output", [
                                            ({"Navn": "big pp", "Adresse": "Bureveien 5", "PostAdr": 1784, "Antall": 1, "Pris": 20, "Bilde": "webadresse.com", "Detaljer": "God utsikt"},
                                             Parkingplace(None, "big pp", "Bureveien 5", 1784, 1, 20, "webadresse.com", "God utsikt")
                                             )
                                        ]
                         )
def test_can_add_new_parking_place_from_dict(p_data, output):
    controller = ParkingController(None, None)

    assert controller.add_parking_place(p_data) == output

