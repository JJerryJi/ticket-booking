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
url1= "https://secure.recreation.ucla.edu/booking/14ded8d8-65d9-405f-8127-ffda2c6b6759"
# JWC - Badminton Ct #2
url2= "https://secure.recreation.ucla.edu/booking/32738a56-3268-4037-98c5-e2d9d6d165d9"
# JWC - Badminton Ct #2
url3= "https://secure.recreation.ucla.edu/booking/24b49a8f-ae2e-4f2e-93ce-0adfbcfbf4f4"
date= "wed"

# initialize the Chrome driver
class autologin():
    def __init__(self,link) -> None:
        self.driver= webdriver.Chrome("./chromedriver")
        self.target_url=link
        self.status = 0 # 0: ticket not booked; 1:ticket booked  

    def setup(self):
        self.driver.get("https://secure.recreation.ucla.edu/booking#")
        time.sleep(0.2)
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.ID, "loginLink")).click()
        WebDriverWait(self.driver, 100).until(lambda x: x.find_element(By.XPATH,"//*[@id='section-sign-in-first']/div[6]/div/button/span/span[2]")).click()

        
        self.driver.find_element(By.ID,"logon").send_keys(username)
        self.driver.find_element(By.ID,"pass").send_keys(password + Keys.ENTER)

        # Bug here
        
        # WebDriverWait(self.driver, 20).until
        #     EC.visibility_of_element_located((By.ID, "sidebar"))
        #     )
        # time.sleep(1)
        # while self.status == 0:
        #     time.sleep(1)
        # WebDriverWait(self.driver, 20).until(lambda x: x.get(self.target_url))
        time.sleep(20)
        self.driver.get(self.target_url)
        
        self.driver.find_element(By.XPATH, "//*[@id='divBookingDateSelector']/div[2]/div[2]/button[2]").click()
    
    
    
    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    a = autologin(url1)
    a.setup()
    a.teardown()











