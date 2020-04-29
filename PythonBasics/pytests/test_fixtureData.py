import pytest

from pytests.BaseClass import BaseClass


@pytest.mark.usefixtures("userData")
class TestData(BaseClass):

    def test_profileData(self, userData):
        log = self.getlogger()
        log.info(userData[0])
        log.info(userData[1])
        log.info(userData[2])
        # print(userData[1])
        # print(userData[0])
        # print(userData[2])


