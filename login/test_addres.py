from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5000)
driver.get("https://practice.automationtesting.in/my-account/")
driver.find_element(By.ID, "username").send_keys("ladalyray13297@gmail.com")
driver.find_element(By.ID, "password").send_keys("@Luckyroy203")
driver.find_element(By.NAME, "login").click()
driver.find_element(By.XPATH, "//a[text()='My Account']").click()
driver.find_element(By.LINK_TEXT, "Addresses").click()
driver.find_element(By.XPATH, "(//a[@class='edit'])[1]").click()

driver.find_element(By.ID, "billing_first_name").send_keys("Priyesh")
driver.find_element(By.ID, "billing_last_name").send_keys("Kumar")
driver.find_element(By.ID, "billing_address_1").send_keys("123 Main Street")
driver.find_element(By.ID, "billing_city").send_keys("Pune")
driver.find_element(By.ID, "billing_postcode").send_keys("411001")
driver.find_element(By.ID, "billing_phone").send_keys("9876543210")
driver.find_element(By.ID, "billing_email").send_keys("testuser@example.com")
driver.find_element(By.NAME, "save_address").click()
