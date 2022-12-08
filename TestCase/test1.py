import pytest
from selenium import webdriver
from Business.login import TestLogin


class Test1:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.login = TestLogin()

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.login.login(self.driver)


if __name__ == '__main__':
    pytest.main(["-sv", __file__])