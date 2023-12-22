import pytest
from Test.test_base import BaseTest
from configuration.config import TestData
from pages.log_in import Log_in
from pages.placing_order import Placeing_Order


class Test_Login(BaseTest):

    def add_to_cart(self):

        self.placeing_order = Placeing_Order(self.driver)
        self.driver.get(TestData.BASE_URL)
        self.placeing_order.placeing_order()


