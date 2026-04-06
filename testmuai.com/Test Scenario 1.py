from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open TestMu AI Selenium Playground
driver.get("https://www.testmuai.com/selenium-playground/")
time.sleep(2)

# Step 2: Click “Simple Form Demo”
driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()
time.sleep(2)

# Step 3: Validate that the URL contains “simple-form-demo”
current_url = driver.current_url
assert "simple-form-demo" in current_url.lower(), f"URL validation failed: {current_url}"
print(" URL validation passed")

# Step 4: Create a variable for a string value
message = "Welcome to TestMu AI"

# Step 5: Enter the variable value in the “Enter Message” text box
driver.find_element(By.ID, "user-message").send_keys(message)

# Step 6: Click “Get Checked Value”
driver.find_element(By.XPATH, "//button[text()='Get Checked Value']").click()
time.sleep(2)

# Step 7: Validate whether the same text message is displayed
output = driver.find_element(By.XPATH, "//p[@id='message']").text
if output == message:
    print(" Message validation passed")
else:
    print(" Message validation failed. Got:", output)

driver.quit()
