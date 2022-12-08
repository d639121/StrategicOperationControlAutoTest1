# Generated by Selenium IDE

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Common.get_code import get_code
from config.get_data import gtd


class TestLogin:

    def __init__(self):
        self._data = gtd.get_data('login.yaml')

    def login(self, driver):
        # Test name: login
        # Step # | name | target | value
        # 1 | open | / |
        data = self._data.get('login')
        url, user, password = gtd.deal_data(data)
        try:
            driver.get(url)
            # 2 | setWindowSize | 1980x1020 |
            driver.set_window_size(1936, 1056)
            # 3 | click | css=.el-form-item:nth-child(1) .el-input__inner |
            driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").click()
            # 4 | click | css=.el-form-item:nth-child(1) .el-input__inner |
            driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").click()
            # 5 | type | css=.el-form-item:nth-child(1) .el-input__inner | qucheng@csg.cn
            driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(1) .el-input__inner").send_keys(
                user)
            # 6 | type | css=.el-form-item:nth-child(2) .el-input__inner | Nfdw@1pa
            driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys(
                password)
            # 7 | type | css=.el-input-group > .el-input__inner | 9571
            driver.implicitly_wait(2)
            code = get_code(driver)
            while code.isdigit() is False or len(code) != 4:
                driver.implicitly_wait(2)
                code = get_code(driver)
            driver.find_element(By.CSS_SELECTOR, ".el-input-group > .el-input__inner").send_keys(code)
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, ".el-input-group > .el-input__inner").send_keys(Keys.ENTER)
            driver.implicitly_wait(5)
            # result = self.driver.find_element(By.CLASS_NAME, "el-message__content").text()
            # assert '成功' in result
        except Exception as msg:
            print(u"异常原因%s" % msg)
            nowTime = time.strftime('%Y%m%d%H%M%S')
            driver.get_screenshot_as_file('%s.png' % nowTime)
            raise


# if __name__ == '__main__':
#     pytest.main(["-sv", __file__])