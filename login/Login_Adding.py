
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3000)
driver.get("https://practice.automationtesting.in/")

#Login steps

driver.find_element(By.XPATH, "//a[text()='My Account']").click()
frame_login=driver.find_element(By.XPATH, "//form[@class='login']")
frame_login.find_element(By.ID, "username").send_keys("ladalyray13297@gmail.com")
frame_login.find_element(By.ID, "password").send_keys("@Luckyroy203")
frame_login.find_element(By.NAME, "login").click()

#Adding into cart
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
element = driver.find_element(By.XPATH, "//h3[text()='Selenium Ruby']//ancestor::a[@class='woocommerce-LoopProduct-link']")
driver.execute_script("arguments[0].scrollIntoView();", element)

element.click()
driver.find_element(By.XPATH, "//button[text()='Add to basket']").click()
driver.find_element(By.XPATH, "//span[@class='cartcontents']").click()

#Remove from cart

driver.find_element(By.XPATH,"(//td[@class='product-remove']/a").click()

#Logout
driver.find_element(By.XPATH, "//a[text()='My Account']").click()
driver.find_element(By.XPATH,"//a[text()='Logout']").click()