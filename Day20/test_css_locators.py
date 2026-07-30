import pytest
from playwright.sync_api import Page , expect

"""
1).tag id ---> tag#id
2).tag class --> tag.class
3).tag attribute --> tag[attribute=value]
4).tag class attribute --> tag.class[attribute=value]


"""


def test_verify_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    # #tag id
    # #page.locator("input#small-searchterms").fill("T-SHIRTS")
    # page.locator("#small-searchterms").fill("T-SHIRTS")
    # page.wait_for_timeout(3000)

    #tag.class
    # page.locator(".search-box-text").fill("Mac-Book")
    # page.wait_for_timeout(3000)

    #tag attribute --> tag[attribute=value]
    # page.locator("[name=q]").fill("I-Phone")
    # page.wait_for_timeout(3000)

    #tag class attribute --> tag.class[attribute=value]
    page.locator(".search-box-text[value='Search store']").fill("T-shirts")
    page.wait_for_timeout(3000)