from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver with ChromeOptions
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
time.sleep(2)


# Open the demoblaze website
driver.get("https://www.demoblaze.com/")
time.sleep(5)