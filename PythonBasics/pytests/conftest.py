import pytest


@pytest.fixture(scope="class")
def setup():
    print("This is pre-execution. This will execute before the actual test")
    yield
    print("This is post-execution. This will execute after the actual test")


@pytest.fixture()
def userData():
    print("User data is displayed")
    return ["Ankit", "Trivedi", "www.twitter.com/ankitptrivedi"]


@pytest.fixture(params=[("Netflix", "Money Heist"), ("Amazon Prime", "All or Nothing"), ("Hotstar", "Metro Town")])
def onlineStreaming(request):
    return request.param

