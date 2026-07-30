"""
pre-requisite : install pytest-order plugin
                install pytest-ordering plugin ==> Deprecated




"""
import pytest

# Approach 1 : order tests by position
#--------------------------------------


# @pytest.mark.order(3)
# def test_logout():
#     print("This is a logout test")
#
# @pytest.mark.order(2)
# def test_add_items():
#     print("This is a add items test")
#
# @pytest.mark.order(1)
# def test_login():
#     print("This is a login test")


# Approach 2 : using  keywords before,after
#-------------------------------------------

#@pytest.mark.order(after="test_add_items")
# def test_checkout():
#     print("This is a checkout test")
#
# @pytest.mark.order(after="test_login")
# def test_add_items():
#     print("This is a add items test")
#
#
# @pytest.mark.order(1)
# def test_login():
#     print("This is a login test")

# Approach 3 : using  marker string (user defined)
#-------------------------------------------


@pytest.mark.order("last")
def test_checkout():
    print("This is a checkout test")




@pytest.mark.order()
def test_add_items():
    print("This is a add items test")


@pytest.mark.order("first")
def test_login():
    print("This is a login test")


