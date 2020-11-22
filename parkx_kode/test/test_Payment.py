import pytest

from parkx_kode.model.Payment import Payment
from parkx_kode.repository.ListRepository import ListRepository


class TestPaymentClass:

    def test_addsNewPaymentProperly(self):
        pass

@pytest.fixture
def paymentObject():
    return Payment(repository)

@pytest.fixture
def repository():
    return ListRepository()

