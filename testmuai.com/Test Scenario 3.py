from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


 # disables save password
options = webdriver.ChromeOptions()
options.add_argument("--disable-save-password-bubble")  
options.add_argument("--disable-autofill")              
options.add_argument("--disable-popup-blocking")

# Initialize the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open Open TestMu
driver.get("https://www.testmuai.com/selenium-playground/")
time.sleep(2)

# Step 2: Click “Input Form Submit”
driver.find_element(By.LINK_TEXT, "Input Form Submit").click()
time.sleep(2)

# Step 3: Click “Submit” without filling in any info
driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)

# Step 4: Validate error message “Please fill out this field.”
name_field = driver.find_element(By.NAME, "name")
error_message = name_field.get_attribute("validationMessage")
if "Please fill out this field" in error_message:
    print("Error validation passed")
else:
    print("Error validation failed. Got:", error_message)

# Step 5: Fill in Name, Email, and other fields
driver.find_element(By.ID, "name").send_keys("Priyesh")
driver.find_element(By.ID, "inputEmail4").send_keys("test@example.com")
driver.find_element(By.ID, "inputPassword4").send_keys("Password123")
driver.find_element(By.ID, "company").send_keys("Test Company")
driver.find_element(By.ID, "websitename").send_keys("https://example.com")

# Step 6: Select “United States” from Country drop-down
country_dropdown = Select(driver.find_element(By.XPATH, "//select[@name='country']"))
country_dropdown.select_by_visible_text("United States")

# Fill in remaining fields
driver.find_element(By.ID, "inputCity").send_keys("New York")
driver.find_element(By.ID, "inputAddress1").send_keys("123 Test Street")
driver.find_element(By.ID, "inputAddress2").send_keys("Suite 456")
driver.find_element(By.ID, "inputState").send_keys("NY")
driver.find_element(By.ID, "inputZip").send_keys("10001")

# Step 7: Submit the form
driver.find_element(By.XPATH, "//button[text()='Submit']").click()
time.sleep(2)

# Step 8: Validate success message
success_message = driver.find_element(By.XPATH, "//p[text()='Thanks for contacting us, we will get back to you shortly.']").text
if "Thanks for contacting us, we will get back to you shortly." in success_message:
    print("Success message validation passed")
else:
    print("Success message validation failed. Got:", success_message)

# Close the browser
driver.quit()