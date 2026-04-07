from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()

# Step 1: Open TestMu
page.goto("https://www.testmuai.com/selenium-playground/")
page.wait_for_timeout(2000)

# Step 2: Click “Input Form Submit”
page.click("text=Input Form Submit")
page.wait_for_timeout(2000)

# Step 3: Click “Submit” without filling in any info
page.click("button:has-text('Submit')")
page.wait_for_timeout(2000)

# Step 4: Validate error message “Please fill out this field.”
name_field = page.query_selector("input[name='name']")
error_message = name_field.evaluate("el => el.validationMessage")
if "Please fill out this field" in error_message:
    print("Error validation passed")
else:
    print("Error validation failed. Got:", error_message)

# Step 5: Fill in Name, Email, and other fields
page.fill("#name", "Priyesh")
page.fill("#inputEmail4", "test@example.com")
page.fill("#inputPassword4", "Password123")
page.fill("#company", "Test Company")
page.fill("#websitename", "https://example.com")

# Step 6: Select “United States” from Country drop-down
page.select_option("select[name='country']", label="United States")

# Fill in remaining fields
page.fill("#inputCity", "New York")
page.fill("#inputAddress1", "123 Test Street")
page.fill("#inputAddress2", "Suite 456")
page.fill("#inputState", "NY")
page.fill("#inputZip", "10001")

# Step 7: Submit the form
page.click("button:has-text('Submit')")
page.wait_for_timeout(2000)

# Step 8: Validate success message
success_message = page.text_content("p:has-text('Thanks for contacting us, we will get back to you shortly.')")
if "Thanks for contacting us, we will get back to you shortly." in success_message:
    print("Success message validation passed")
else:
    print("Success message validation failed. Got:", success_message)

# Close browser
browser.close()
playwright.stop()