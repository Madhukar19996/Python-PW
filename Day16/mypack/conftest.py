import pytest

@pytest.fixture()
def setup():
    print("setup environment")
    yield
    print("tear down..")