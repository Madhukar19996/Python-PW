import pytest

@pytest.mark.skip
def test_loginbyemail():
    print("This is login  by email test")
    assert 1 == 1

@pytest.mark.skip
def test_loginbyfacebook():
    print("This is login  by facebook test")
    assert 1 == 1


def test_loginbynumber():
    print("This is login  by number test")
    assert 1 == 1


def test_signupbyemail():
    print("This is signup  by email test")
    assert 1 == 1

@pytest.mark.skip
def test_signupbyfacebook():
    print("This is signup  by facebook test")
    assert 1 == 1

@pytest.mark.skip
def test_signupbyphone():
    print("This is signup  by phonr test")
    assert 1 == 1
