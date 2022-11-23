from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

# credentials
username = "jerryji040506"
password = "Jzx20040506!!"
# JWC - Badminton Ct #1
url1= "https://secure.recreation.ucla.edu/booking/b2f7d448-aaff-4d93-969f-2083fa1cb9e3"
# JWC - Badminton Ct #2
url2= "https://secure.recreation.ucla.edu/booking/32738a56-3268-4037-98c5-e2d9d6d165d9"
# JWC - Badminton Ct #2
url3= "https://secure.recreation.ucla.edu/booking/24b49a8f-ae2e-4f2e-93ce-0adfbcfbf4f4"
date= "wed"

# initialize the Chrome driver
driver = webdriver.Chrome()


driver.get("https://secure.recreation.ucla.edu/booking#")

WebDriverWait(driver, 10).until(lambda x: x.find_element(By.ID, "loginLink")).click()


WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH,"//*[@id='section-sign-in-first']/div[6]/div/button/span/span[2]")).click()
# driver.find_element(By.XPATH,"//*[@id='section-sign-in-first']/div[6]/div/button/span/span[2]").click()

driver.find_element(By.ID,"logon").send_keys(username)
driver.find_element(By.ID,"pass").send_keys(password + Keys.ENTER)







WebDriverWait(driver,200).until(lambda x: x.find_element(By.XPATH, "//*[@id='divBookingProducts-small']/div[2]/a")).click()
elements = driver.find_elements(By.CSS_SELECTOR,"Button.btn single-date-select-button single-date-select-one-click btn-primary")
for e in elements:
    if(e.get_attribute("data-date-text")=="Nov 23, 2022"):
        e.click()




driver.close()




