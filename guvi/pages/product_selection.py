from pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


class Product_Selection:

    def __init__(self, driver):
        self.driver = driver

    def product_selection(self):
        time.sleep(5)
        # click Phone
        button_xpath = "/html/body/div[5]/div/div[1]/div/a[2]"
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )
        button.click()

        # Select Phone
        button_xpath = "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a"
        button = self.driver.find_element(By.XPATH, button_xpath)
        button.click()
        time.sleep(7)
        # click add to cart
        button_xpath = "/html/body/div[5]/div/div[2]/div[2]/div/a"
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )
        button.click()
        time.sleep(5)


        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_message = alert.text
        expected_alert_message = "Product added."

        assert alert_message == expected_alert_message, f"Actual alert message: {alert_message}"

        # Accept the alert
        alert.accept()



        # try:
        #     WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        #     alert = self.driver.switch_to.alert
        #     alert.accept()
        # except NoAlertPresentException:
        #     pass  # No alert present, continue with the next steps


    def is_product_added_to_cart(self):
        try:
            # Wait for an element that is only present when the login is successful
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div[2]/button"))
            )
            return True  # If the element is found, consider the login successful
        except:
            return False