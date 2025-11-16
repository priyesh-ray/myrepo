from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5000)
driver.get("https://practice.automationtesting.in/")
driver.find_element(By.XPATH, "//a[text()='My Account']").click()
Registration_frame=driver.find_element(By.XPATH, "//form[@class='register']")
Registration_frame.find_element(By.ID, "reg_email").send_keys("ladalyray13297@gmail.com")
Registration_frame.find_element(By.ID, "reg_password").send_keys("@Luckyroy203")
Registration_frame.find_element(By.NAME, "register").click()