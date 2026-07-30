from playwright.sync_api import Page, expect


def test_verifyPageUrl(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  #passing url

    myurl=page.url
    print("Url of the application :", myurl)
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") #expected url

def test_verifyPageTittle(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    pagetitle=page.title()
    print("Title of the page :",pagetitle)
    expect(page).to_have_title("OrangeHRM")

