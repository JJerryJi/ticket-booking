from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# credentials
username = "jerryji040506"
password = "Jzx20040506!!"

# initialize the Chrome driver
driver = webdriver.Chrome()


driver.get("https://secure.recreation.ucla.edu/booking#")

WebDriverWait(driver, 100).until(lambda x: x.find_element(By.ID, "loginLink")).click()

#need to improve efficiency
time.sleep(1)

driver.find_element(By.XPATH,"//*[@id='section-sign-in-first']/div[6]/div/button/span/span[2]").click()

driver.find_element(By.ID,"logon").send_keys(username)

driver.implicitly_wait(10)

WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID,"pass").send_keys(password + Keys.ENTER))

driver.implicitly_wait(10)
WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, 'container-image-item booking-product-image')).click()

time.sleep(2)
driver.close()



