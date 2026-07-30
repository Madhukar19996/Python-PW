import pytest



@pytest.fixture()
def setup():
    print("Setup browser...")
    return "chrome"

def test_mytest_one(setup):
    print("This is my test one ")
    print("Browser is:", setup)


def test_mytest_two(setup):
    print("This is my test two")
    print("Browser is:", setup)


def test_mytest_three(setup):
    print("This is my test three")
    print("Browser is:", setup)