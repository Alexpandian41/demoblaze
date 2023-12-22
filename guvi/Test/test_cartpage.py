import time

import pytest
from Test.test_base import BaseTest
from configuration.config import TestData
from pages.log_in import Log_in
from pages.cartpage import Cartpage
from pages.placing_order import Placeing_Order


class Test_cart(BaseTest):

    def test_cartpage(self):
        # Login
        self.log_in = Log_in(self.driver)
        self.driver.get(TestData.BASE_URL)
        self.log_in.log_in(TestData.USER_NAME, TestData.PASSWORD)

        self.placeing_order = Placeing_Order(self.driver)
        self.driver.get(TestData.BASE_URL)
        self.placeing_order.placeing_order()


        time.sleep(5);

        # Perform actions after logging in
        # assert self.log_in.is_logged_in()  # Add an assertion to verify login success
        # Add product to cart
        self.add_cart = Cartpage(self.driver)
        self.driver.get(TestData.BASE_URL)
        self.add_cart.enterCartDetails('Alex', 'India', 'Tel', '1234567', 'June', '2023')

