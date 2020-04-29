import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture(self):
        print("This is the actual code.")

    def test_fixture1(self):
        print("This is the actual code 1.")

    def test_fixture2(self):
        print("This is the actual code 2.")

    def test_fixture3(self):
        print("This is the actual code 3.")