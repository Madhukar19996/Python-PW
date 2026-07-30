# # import re
# # import time
# #
# # from playwright.sync_api import Page, expect
# #
# # def test_verify_login_functionality(page: Page):
# #     page.goto(
# #         "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
# #         timeout=60000
# #     )
# #     Username_inputbox=page.get_by_placeholder("Username")
# #     Username_inputbox.fill("Admin")
# #     page.wait_for_timeout(1000)
# #     Password_inputbox = page.get_by_placeholder("Password")
# #     Password_inputbox.fill("admin123")
# #     page.wait_for_timeout(1000)
# #     Login_Btn=page.get_by_role('button')
# #     Login_Btn.click()
# #     page.wait_for_timeout(4000)
# #
# #     Dashboad_text=expect(page.locator('h6:has-text("Dashboard")'))
# #     #print(Dashboad_text)
# #     page.wait_for_timeout(3000)
# #     print("Test case passed ")
# #
# #
# #
# #
# from playwright.sync_api import Page, expect
#
#
# def test_verify_login_functionality(page: Page):
#
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#     page.get_by_placeholder("Username").fill("Admin")
#     page.get_by_placeholder("Password").fill("admin123")
#     page.get_by_role("button", name="Login").click()
#
#     expect(page.locator("h6")).to_have_text("Dashboard")
#
from asyncio import timeout

from playwright.sync_api import Page, expect


def test_verify_login_functionality(page: Page):

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",timeout=60000)


    # Fill login credentials
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    # Click login button
    page.get_by_role("button", name="Login").click()

    # Validate dashboard is visible
    expect(page.locator("h6")).to_have_text("Dashboard")

    print("Test case passed")