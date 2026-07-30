"""
grouping tests
==============
test_LoginByEmail --> sanity,regression
test_LoginByFacebook --> sanity
test_LoginByPhone --> regression
test_SignupByEmail --> sanity,regression
test_SignupByFacebook --> regression
test_SignupByPhone --> sanity
test_paymentindollar --> sanity, regression
test_paymentinrupees --> regression

"""
import pytest

#@pytest.mark.skip
@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    print("This is login  by email test")
    assert 1 == 1


@pytest.mark.sanity
def test_loginbyfacebook():
    print("This is login  by facebook test")
    assert 1 == 1

@pytest.mark.regression
def test_loginbynumber():
    print("This is login  by number test")
    assert 1 == 1

@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyemail():
    print("This is signup  by email test")
    assert 1 == 1


@pytest.mark.regression
def test_signupbyfacebook():
    print("This is signup  by facebook test")
    assert 1 == 1


@pytest.mark.sanity
def test_signupbyphone():
    print("This is signup  by phonr test")
    assert 1 == 1


@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollar():
    print("This is a payment in dollar test")
    assert 1 == 1


@pytest.mark.regression
def test_paymentinrupees():
    print("This is a payment in rupees test")
    assert 1 == 1

"""
1) Run sanity tests = 5 passed, 3 deselected in 0.03s
   pytest Day17/test_grouping.py -v -s -m "sanity"

2) Run regression tests = 6 passed, 2 deselected in 0.03s
   pytest Day17/test_grouping.py -v -s -m "regression"

3) run test  which are belongs to both sanity and regression = 3 passed, 5 deselected in 0.02s
   pytest Day17/test_grouping.py -v -s -m "sanity and regression"
   
4) run only sanity test which are not belongs to regression = 2 passed, 6 deselected in 0.02s
   pytest Day17/test_grouping.py -v -s -m "sanity" -m "not regression" 

5) run only regression test which are not belongs to sanity = 3 passed, 5 deselected in 0.02s
   pytest Day17/test_grouping.py -v -s -m "regression" -m "not sanity"
   
"""
