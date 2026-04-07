import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Step 1: Open TestMu
        await page.goto("https://www.testmuai.com/selenium-playground/")
        await page.wait_for_timeout(2000)

        # Step 2: Click “Simple Form Demo”
        await page.click("text=Simple Form Demo")
        await page.wait_for_timeout(2000)

        # Step 3: Validate that the URL contains “simple-form-demo”
        current_url = page.url
        assert "simple-form-demo" in current_url.lower(), f"URL validation failed: {current_url}"
        print("URL validation passed")

        # Step 4: Create a variable for a string value
        message = "Welcome to TestMu AI"

        # Step 5: Enter the variable value in the “Enter Message” text box
        await page.fill("#user-message", message)

        # Step 6: Click “Get Checked Value”
        await page.click("button:text('Get Checked Value')")
        await page.wait_for_timeout(2000)

        # Step 7: Validate whether the same text message is displayed
        output = await page.locator("//p[@id='message']").text_content()
        if output == message:
            print("Message validation passed")
        else:
            print("Message validation failed. Got:", output)
#close the browser
        await browser.close()

asyncio.run(run())
