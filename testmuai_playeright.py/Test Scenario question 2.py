from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Open TestMu
        page.goto("https://www.testmuai.com/selenium-playground/")
        page.wait_for_timeout(2000)

        # Step 2: Click “Drag & Drop Sliders”
        page.click("text=Drag & Drop Sliders")
        page.wait_for_timeout(2000)

        # Step 3: Select the slider “Default value 15”
        slider = page.locator("//input[@type='range' and @value='15']")
        range_value = page.locator("#rangeSuccess")

        # Step 4: Drag the slider to 95
        slider.evaluate("el => el.value = 95")
        page.wait_for_timeout(5000)
        slider = page.locator("//input[@type='range' and @value='95']")
        range_value = page.locator("#rangeSuccess")
        page.wait_for_timeout(2000)

        # Step 5: Validate whether the range value shows 95
        output = range_value.text_content()
        if output == "95":
            print("Slider validation passed")
        else:
            print("Slider validation failed. Current value:", output)

        browser.close()

if __name__ == "__main__":
    run()
