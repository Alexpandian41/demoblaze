from pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys



class Sign_Up:
    USERNAME_INPUT = (By.ID, "sign-username")  # Replace "sign-username" with the actual ID of your username input
    PASSWORD_INPUT = (By.ID, "sign-password")  # Replace "sign-password" with the actual ID of your password input

    def __init__(self, driver):
        self.driver = driver

    def signup(self, username, password):
        time.sleep(5)
        signup_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signin2"))
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

        button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]//button[2]")
        button.click()
        time.sleep(3)
