import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    print("Hello")


@pytest.mark.xfail
def test_secondprogram():
    print("Good Morning")


def test_streaming(onlineStreaming):
    print(onlineStreaming[1])

