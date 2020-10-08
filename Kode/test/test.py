from core.main import *

x = Bruker()


def test_receive_hello():
    assert x.return_print() == "Hello world"

