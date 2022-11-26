from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


# UCLA credentials
username = "UCLA Logon UserName"
password = "UCLA Logon Password"


# JWC - Badminton Ct #1
url1 = "https://secure.recreation.ucla.edu/booking/14ded8d8-65d9-405f-8127-ffda2c6b6759"
# JWC - Badminton Ct #2
url2 = "https://secure.recreation.ucla.edu/booking/32738a56-3268-4037-98c5-e2d9d6d165d9"
# JWC - Badminton Ct #2
url3 = "https://secure.recreation.ucla.edu/booking/24b49a8f-ae2e-4f2e-93ce-0adfbcfbf4f4"

# initialize the Chrome driver


class autologin():
    def __init__(self, link) -> None:
        self.driver = webdriver.Chrome()
        self.target_url = link
        self.status = 0

    def setup(self):
        time.sleep(0.2)
        self.driver.get("https://secure.recreation.ucla.edu/booking#")
        time.sleep(0.2)
        WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element(By.ID, "loginLink")).click()
        WebDriverWait(self.driver, 100).until(lambda x: x.find_element(
            By.XPATH, "//*[@id='section-sign-in-first']/div[6]/div/button/span/span[2]")).click()

        time.sleep(0.2)
        self.driver.find_element(By.ID, "logon").send_keys(username)
        time.sleep(0.2)
        self.driver.find_element(By.ID, "pass").send_keys(
            password + Keys.ENTER)

        # Hardcode this to wait for Duo-Push from Iphone
        time.sleep(20)
        # after signing in, going to the page to select field
        self.driver.get(self.target_url)

        self.validate_state(
            self.driver, "//*[@id='divBookingDateSelector']/div[2]/div[2]/button[2]")

        # Line 49-50 is equivalent to Line 46
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, "//*[@id='divBookingDateSelector']/div[2]/div[2]/button[2]").click()

        # time.sleep(2)

        self.check_availablity()

        while True:
            # self.driver.find_element(By.XPATH, "//button[contains(text(),'Book Now')]").click()
            # time.sleep(1)
            self.validate_state(
                self.driver, "//button[contains(text(),'Book Now')]")
            # wait for the element to be clickable
            time.sleep(1)
            if self.driver.find_element(By.XPATH, "//span[contains(text(),'Booked')]").is_displayed():
                print("success")
                break

    # Helper function that make sure every element is clickable in the website; then click

    def validate_state(self, pramWebdriver, xpath):
        wait = WebDriverWait(pramWebdriver, 10)
        elm = wait.until(lambda x: x.find_element(
            By.XPATH, xpath).is_displayed())
        elm = wait.until(lambda x: x.find_element(By.XPATH, xpath))
        elm.click()

    def check_availablity(self):
        time.sleep(0.2)
        if self.driver.find_element(By.XPATH, "//div[contains(text(),'Sorry, there are no available times. Please try another day or location.')]").is_displayed():
            print("No available spots")
            self.teardown

    # close the browser

    def teardown(self):
        self.driver.close()


if __name__ == '__main__':
    court = input(
        "Which field you wanna chooose? Please respond in 1, 2, 3? ----- Your answer: ")

    if court == "1":
        a = autologin(url1)
        a.setup()
        a.teardown()
    elif court == "2":
        a = autologin(url2)
        a.setup()
        a.teardown()
    elif court == "3":
        a = autologin(url3)
        a.setup()
        a.teardown()
