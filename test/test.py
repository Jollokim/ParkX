from core.main import *

x = Bruker()


def test_welcome_message():
    assert x.print_welcome() == "Hello world"
