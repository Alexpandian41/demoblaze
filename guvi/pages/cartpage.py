from pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException


class Cartpage:

    def __init__(self, driver):
        self.driver = driver

    def enterCartDetails(self,Name, Country, City, CreditCard, Month, Year):
        # Wait for an element that is only present when the login is successful
        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[4]/a"))
        )

        button.click()

        time.sleep(5)


        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div[2]/button"))
        )

        button.click()

        time.sleep(5)

        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[1]/input").send_keys(Name)
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[2]/input").send_keys(Country)
        self.driver.implicitly_wait(5)


        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[3]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[3]/input").send_keys(City)
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[4]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[4]/input").send_keys(CreditCard)
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[5]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[5]/input").send_keys(Month)
        self.driver.implicitly_wait(5)

        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[6]/input").clear()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[2]/form/div[6]/input").send_keys(Year)
        self.driver.implicitly_wait(5)

        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]"))
        )

        button.click()

        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/h2"))
        )

        button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[10]/div[7]"))
        )

        button.click()

        time.sleep(5)



