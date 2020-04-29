import pytest


@pytest.mark.smoke
# @pytest.mark.xfail
def test_firstprogram():
    msg = "Hello"
    assert msg == "Hi", "Assertion failed"


def test_secondprogram():
    a = 4
    b = 6
    assert a + 2 == b, "Assertion failed"
