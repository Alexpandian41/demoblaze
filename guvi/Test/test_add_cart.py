import pytest
from Test.test_base import BaseTest
from configuration.config import TestData
from pages.log_in import Log_in
from pages.product_selection import Product_Selection


class Test_Login(BaseTest):

    def test_login_and_add_to_cart(self):
        # Login
        # self.log_in = Log_in(self.driver)
        # self.driver.get(TestData.BASE_URL)
        # self.log_in.log_in(TestData.USER_NAME, TestData.PASSWORD)

        # Perform actions after logging in
        # assert self.log_in.is_logged_in()  # Add an assertion to verify login success
        # Add product to cart
        self.add_cart = Product_Selection(self.driver)
        self.driver.get(TestData.BASE_URL)
        self.add_cart.product_selection()

        # Assertions after adding to cart
        # assert self.add_cart.is_product_added_to_cart()  # Add an assertion for successful addition to cart

        # Additional assertions or actions can be added as needed

