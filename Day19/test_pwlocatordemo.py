"""
1).page.getByRole() => to locate by explicit and implicit accessibility attributes.
2).page.getByText() => to locate by text content.
3).page.getByLabel()=> to locate a form control by associated label's text.
4).page.getByPlaceholder() => to locate an input by placeholder.
5).page.getByAltText() => to locate an element, usually image, by its text alternative.
6).page.getByTitle()  => to locate an element by its title attribute.
7).page.getByTestId() =>  to locate an element based on its data-testid attribute (other attributes can be configured).
"""
import re
import time

from playwright.sync_api import Page, expect


def test_verify_pwlocator(page: Page):
    page.goto("https://demo.nopcommerce.com/")
    # time.sleep(3) # seconds
    page.wait_for_timeout(3000)  # miliseconds 3000ms=3sec

    # 1) page.getByAltText()
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    # 2) page.getByText()
    expect(page.get_by_text("Welcome to our store")).to_be_visible()  # full text
    expect(page.get_by_text("Welcome to ")).to_be_visible()  # partial text
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()  # reg expression

    # 3) page.getByRole()


def test_verify_page_getByRole(page: Page):
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    page.wait_for_timeout(3000)  # miliseconds 3000ms=3sec
    expect(page.get_by_role("heading", name="Register")).to_be_visible()

    # 4) page.getByLabel()


def test_verify_page_getByLabel(page: Page):
    page.goto("https://demo.nopcommerce.com/register?returnUrl=%2F")
    # time.sleep(3) # seconds
    page.wait_for_timeout(3000)  # miliseconds 3000ms=3sec

    # 4) page.getByLabel()
    page.get_by_label("First name:").fill("Madhukar")
    page.get_by_label("Last name:").fill("Pandey")
    page.get_by_label("Email:").fill("Test@123gmail.com")
    page.wait_for_timeout(3000)

    # 5) page.getByPlaceholder()
    searchbox = page.get_by_placeholder("Search store").fill("Apple MacBook Pro")
    # expect(searchbox).to_be_visible()
    page.wait_for_timeout(3000)


def test_verify_page_getByTitle(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    page.wait_for_timeout(3000)


def test_verify_page_getByTitle(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(3000)


   #7).page.getByTestId()
def test_verify_page_getByTestId(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")
    page.wait_for_timeout(3000)
