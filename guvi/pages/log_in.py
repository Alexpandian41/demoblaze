from pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


class Log_in:
    USERNAME_INPUT = (By.ID, "loginusername")
    PASSWORD_INPUT = (By.ID, "loginpassword")

    def __init__(self, driver):
        self.driver = driver

    def log_in(self, username, password):
        time.sleep(5)
        signup_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login2"))
        )

        # Once the element is clickable, perform the click
        signup_link.click()

        time.sleep(5)


        username_input = self.driver.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)

        # Enter password
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)

        # Submit the form (if there's a submit button, otherwise, adapt as needed)
        password_input.send_keys(Keys.RETURN)

        button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
        button.click()
        time.sleep(8)


    def is_logged_in(self):
        try:
            # Wait for an element that is only present when the login is successful
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "nameofuser"))
            )
            return True  # If the element is found, consider the login successful
        except:
            return False  # If the ele