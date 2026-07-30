from playwright.sync_api import Page, expect
import re


def test_verifyPageUrl(page:Page):
    page.goto("https://www.amazon.in/")  #passing url

    myurl=page.url
    print("Url of the application :", myurl)
    expect(page).to_have_url("https://www.amazon.in/") #expected url

def test_verifyPageTittle(page:Page):
    page.goto("https://www.amazon.in/")

    pagetitle=page.title()
    print("Title of the page :",pagetitle)
    expect(page).to_have_title(re.compile("Amazon"))

# command :  pytest Day18-PW/test_playwright_firebox.py -v -s --headed --browser firefox
#            pytest Day18-PW/test_playwright_firebox.py -v -s --headed --browser firefox --browser chromium
#            pytest Day18-PW/test_playwright_firebox.py -v -s --headed --browser firefox --browser chromium --numprocesses=2



