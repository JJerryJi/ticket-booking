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


driver.find_element(By.ID,"loginLink").click()

time.sleep(3)

driver.find_element(By.XPATH,"//*[@id='section-sign-in-first']/div[6]/div/button/span/span[2]").click()

time.sleep(3)

driver.find_element(By.ID,"logon").send_keys(username)
driver.find_element(By.ID,"pass").send_keys(password + Keys.ENTER)

element = WebDriverWait(driver, 20).until(lambda x: x.find_element(By.ID, 'container-image-item booking-product-image'))

element.click()

time.sleep(2)
driver.close()




