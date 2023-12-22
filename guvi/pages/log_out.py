from pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


class Log_out:

    def __init__(self, driver):
        self.driver = driver

    def log_out(self):
        time.sleep(5)
        log_out_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout2"))
        )

        # Once the element is clickable, perform the click
        log_out_link.click()

        time.sleep(5)


    def is_log_out(self):
        try:
            # Wait for an element that is only present when the login is successful
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "nameofuser"))
            )
            return True  # If the element is found, consider the login successful
        except:
            return False  # If the ele