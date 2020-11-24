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

    def test_addsNewPaymentProperly(self, paymentObject, payment_dict):
        assert len(paymentObject.repository.payments) == 0

        paymentObject.add_new_payment(**payment_dict)
        savedPayment = paymentObject.repository.payments[0]
        for key in savedPayment.keys():
            assert payment_dict.get(key) == savedPayment.get(key)

        assert len(paymentObject.repository.payments) == 1

    def test_paysAllPaymentsProperly(self, paymentObject, payment_dict):
        paymentObject.add_new_payment(**payment_dict)
        assert len(paymentObject.repository.payments) == 1
        paymentObject.change_accepted_payment_details(True)

        paymentObject.pay_all_payments()
        assert len(paymentObject.repository.payments) == 0

    def test_returnsProperPaymentDetailsBooleanValue(self, paymentObject):
        expected = paymentObject.acceptedPaymentDetails
        actual = paymentObject.check_accepted_payment_details()
        assert expected == actual

        paymentObject.acceptedPaymentDetails = True
        expected = paymentObject.acceptedPaymentDetails
        actual = paymentObject.check_accepted_payment_details()

        assert expected == actual


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