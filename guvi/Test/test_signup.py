import pytest
from Test.test_base import BaseTest
from configuration.config import TestData
from pages.sign_up import Sign_Up

class Test_SignUp(BaseTest):

    def test_signup_new_user(self):
        self.sign_up = Sign_Up(self.driver)
        self.driver.get(TestData.BASE_URL)
        self.sign_up.signup(TestData.USER_NAME, TestData.PASSWORD)

