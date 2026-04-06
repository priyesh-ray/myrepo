from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Initialize the browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open Open TestMu
driver.get("https://www.testmuai.com/selenium-playground/")
time.sleep(2)

# Step 2: Click “Drag & Drop Sliders”
driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()
time.sleep(2)

# Step 3: Select the slider “Default value 15”
slider = driver.find_element(By.XPATH, "//input[@type='range' and @value='15']")
range_value = driver.find_element(By.XPATH, "//output[@id='rangeSuccess']")

# Drag the slider to 95
action = ActionChains(driver)
action.click_and_hold(slider).move_by_offset(240, 0).release().perform()
time.sleep(3)

# Step 4: Validate whether the range value shows 95
if range_value.text == "95":
    print("Slider validation passed")
else:
    print("Slider validation failed. Current value:", range_value.text)
 
# Close the browser
driver.quit()
