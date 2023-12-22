# import pytest
#
# from selenium import webdriver
from configuration.config import TestData
#
#
# @pytest.fixture(params=["chrome"], scope='class')
# def init_driver(request):
#
#     if request.param == "chrome":
#
#         web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
#     # if request.param == "firefox":
#     #     web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()
#
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import ChromeOptions
# from path.to.config_module import TestData  # Import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        # Set the path to the ChromeDriver executable
        chrome_options.add_argument(f"executable_path={TestData.CHROME_EXECUTABLE_PATH}")

        # Create Chrome WebDriver instance with the configured options
        web_driver = webdriver.Chrome(options=chrome_options)

    request.cls.driver = web_driver
    yield
    web_driver.quit()
