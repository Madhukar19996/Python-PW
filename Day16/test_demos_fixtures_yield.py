import pytest



@pytest.fixture()
def setup():
    print("Setup browser...")
    yield
    print("close browser...")

def test_mytest_one(setup):
    print("This is my test one ")


def test_mytest_two(setup):
    print("This is my test two")


def test_mytest_three(setup):
    print("This is my test three")