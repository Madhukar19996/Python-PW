import pytest
from playwright.async_api import async_playwright, expect
"""
pre-requites : To run async test we ned to install pytest-asyncio first 
command :pip install pytest-asyncio

"""
@pytest.mark.asyncio
async def test_verifyPageUrl():

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
            wait_until="domcontentloaded",
            timeout=60000
        )

        await expect(page).to_have_url(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        await browser.close()