import pytest

from parkx_kode.model.Payment import Payment
from parkx_kode.repository.ListRepository import ListRepository


class TestPaymentClass:

    def test_changesPaymentDetailsBoolCorrectly(self, paymentObject):
        assert paymentObject.acceptedPaymentDetails is False

        paymentObject.change_accepted_payment_details(True)
        assert paymentObject.acceptedPaymentDetails is True

        paymentObject.change_accepted_payment_details(False)
        assert paymentObject.acceptedPaymentDetails is False






@pytest.fixture
def paymentObject():
    return Payment(ListRepository())

@pytest.fixture
def payment_dict():
    return {
            "name": "payment1",
            "parkingStarted": "20:00:00",
            "parkingStopped": "21:00:00",
            "price": "100"
        }