import pytest
from Test.test_base import BaseTest
from configuration.config import TestData
from pages.log_in import Log_in
from pages.log_out import Log_out

class Test_Login(BaseTest):

    def test_login(self):
        self.log_in = Log_in(self.driver)
        self.driver.get(TestData.BASE_URL)
        self.log_in.log_in(TestData.USER_NAME, TestData.PASSWORD)


    def test_logout(self):
        self.log_out = Log_out(self.driver)
        self.driver.get(TestData.BASE_URL)
        self.log_out.log_out()



