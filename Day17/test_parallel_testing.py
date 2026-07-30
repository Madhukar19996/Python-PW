"""
pre-requisite : Install a pytest plugin "pytest-xdist" to run  tests parallel
                pip install pytest-xdist

To run the test parallely :pytest Day17/test_parallel_testing.py -v -s  -n 2
                           pytest Day17/test_parallel_testing.py -v -s  -n=2

"""


import pytest

def test_one():
    print("Running test one")
    assert True


def test_two():
    print("Running test two")
    assert True

def test_three():
    print("Running test three")
    assert True
def test_four():
    print("Running test four")
    assert True